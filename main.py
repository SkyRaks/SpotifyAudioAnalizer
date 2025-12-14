import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
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

        self.button = QPushButton("click me", self)
        self.label = QLabel("what is the genre of Mettalica?", self)

        self.initUi()

    def initUi(self):
        self.button.setGeometry(200, 150, 100, 50)
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(70, 250, 500, 50)
        self.label.setStyleSheet("font-size: 30px")
        
    
    def on_click(self):
        # genre = scripts.get_artist(token, "Metallica")
        self.label.setText(scripts.get_artist(token, "Metallica"))

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MinWindow()
    window.show()
    sys.exit(app.exec_())

