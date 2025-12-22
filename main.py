import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
import scripts

token = scripts.get_token()
# genre = scripts.get_artist(token, "Metallica")

# app should analyze songs by tempo, energy, danceability
# tech stack: spotipy?, matplotlib, plotly

class MinWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AudioAnalyzer")
        self.setGeometry(700, 300, 500, 500)

        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.label = QLabel("Get params of your song", self)

        self.initUi()

    def initUi(self):
        self.line_edit.setGeometry(100, 10, 200, 40)
        self.line_edit.setPlaceholderText("enter song name")
        self.button.setGeometry(300, 10, 110, 40)
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(80, 250, 500, 50)
        self.label.setStyleSheet("font-size: 30px")
        
    
    def on_click(self):
        song_name = self.line_edit.text()
        features = scripts.get_song_feachures(song_name)
        if features == 429:
            self.label.setText("i'm out of free requests(")
            return

        tempo = features[0]
        energy = features[1]
        danceability = features[2]

        self.label.setText(f"tempo: {tempo}, energy: {energy}, danceability: {danceability}")

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MinWindow()
    window.show()
    sys.exit(app.exec_())

