import json
from pprint import pprint

import requests
from dotenv import load_dotenv
import os
import base64

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
base_url = "https://accounts.spotify.com"

def get_token():
    client_string = client_id + ":" + client_secret
    client_bytes = client_string.encode("utf-8")
    client_64 = str(base64.b64encode(client_bytes), "utf-8")

    url = base_url + "/api/token"
    headers = {
        "Authorization": "Basic " + client_64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    # json_result = json.loads(result.content)
    if response.status_code == 200:
        json_result = json.loads(response.content)
        return json_result["access_token"]
    else:
        return f"failed to renrieve data status code: {response.status_code}"

def get_header(token):
    return {"Authorization": "Bearer " + token}

def get_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query

    response = requests.get(query_url, headers=headers)
    if response.status_code == 200:
        json_response = json.loads(response.content)
        pprint(json_response)
    else:
        print(f"failed to get data, status code: {response.status_code}")

token = get_token()
get_artist(token, "Metallica")