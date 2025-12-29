import json
from pprint import pprint
import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

rapid_api_key = os.getenv("rapid_api_key")
rapid_url = "https://track-analysis.p.rapidapi.com/pktx/spotify/"

base_url = "https://accounts.spotify.com"
search_url = "https://api.spotify.com/v1/search"

# this is getting token required by spotify api
def get_token():
    client_string = f"{client_id}:{client_secret}"
    client_bytes = client_string.encode("utf-8") # all of this is needed to encode stuff
    client_64 = str(base64.b64encode(client_bytes), "utf-8")

    url = base_url + "/api/token"
    headers = {
        "Authorization": "Basic " + client_64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        token = response.json()["access_token"]
        return token
    else:
        return f"failed to renrieve data status code: {response.status_code}, {response.text}"

def get_header(token):
    return {"Authorization": f"Bearer {token}"}

# this is method to get url to search for artists params
def get_artist(token, artist_name):
    headers = get_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = search_url + query

    response = requests.get(query_url, headers=headers)
    if response.status_code == 200:

        json_response = json.loads(response.content)
        pprint(json_response['artists']['items'][0]['genres'][0])
        genre = json_response['artists']['items'][0]['genres'][0]
        return genre
    else:
        print(f"failed to get data, status code: {response.status_code}")

def get_song_id(song_name, token):
    # token = get_token()
    headers = get_header(token)
    query = f"?q={song_name}&type=track&limit=1"
    query_url = search_url + query

    response = requests.get(query_url, headers=headers)
    if response.status_code == 200:

        json_response = response.json()
        song = json_response['tracks']['items'][0]['id'] # song id
        return song
    else:
        print(f"failed to get data, status code: {response.status_code}")

def get_song_feachures(song_name):
    token = get_token()
    song_id = get_song_id(song_name, token)

    url = f"{rapid_url}{song_id}"
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "track-analysis.p.rapidapi.com"
    }

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        features = []
        
        res = response.json()
        features.append(res["tempo"])
        features.append(res["energy"])
        features.append(res["danceability"])

        return features
    else:
        return response.status_code

# pprint(get_song_feachures("Psychosocial"))
