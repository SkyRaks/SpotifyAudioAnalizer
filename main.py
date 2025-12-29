import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget, QGridLayout
from PyQt5.QtCore import Qt
import scripts
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

token = scripts.get_token()
# app should analyze songs by tempo, energy, danceability
# tech stack: spotipy?, matplotlib, plotly

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AudioAnalyzer")
        self.setGeometry(700, 300, 500, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vLayout = QVBoxLayout(central_widget)
        hLayout = QHBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("enter song name")
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.on_click)

        self.charts = Canvas()
        vLayout.addLayout(hLayout)
        vLayout.addWidget(self.charts)

        self.initUi()

    def initUi(self):
        self.line_edit.setGeometry(100, 10, 200, 40)
        self.button.setGeometry(300, 10, 110, 40)

    def on_click(self):
        # song_name = self.line_edit.text()
        # features = scripts.get_song_feachures(song_name)
        # if features == 429:
        #     # self.label.setText("i'm out of free requests(")
        #     print("i'm out of free requests(")
        #     return
        
        # tempo = features[0]
        # energy = features[1]
        # danceability = features[2]

        # Canvas.update_values(self, 120, 50, 70)
        self.charts.update_values(120, 50, 70)

        # print(f"tempo: {tempo}, energy: {energy}, danceability: {danceability}")

class Canvas(FigureCanvasQTAgg):
    params = ["tempo", "energy", "danceability"]
    values = [0, 0, 0]

    def __init__(self):
        fig, self.ax = plt.subplots(figsize=(4,3))
        self.ax.bar(self.params, self.values)
        super().__init__(fig)

        self.draw_charts()

    def draw_charts(self):
        self.ax.clear()
        self.ax.bar(self.params, self.values)
        self.draw()

    def update_values(self, tempo, energy, danceability):
        self.values = [tempo, energy, danceability]
        self.draw_charts()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

