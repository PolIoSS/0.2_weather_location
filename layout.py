import os
import requests
import webbrowser
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout
from PyQt6.QtGui import QKeySequence, QPainter, QPixmap, QShortcut
from PyQt6.QtCore import Qt

class Website(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")
        self.resize(900, 700)

        self.background = QPixmap(os.path.join(os.path.dirname(__file__), "background.png"))

        layout = QGridLayout()
        self.setLayout(layout)



        button1= QPushButton("Google")
        button1.setFixedSize(160, 60)
        def open_google():
            webbrowser.open('http://www.google.com')
        button1.clicked.connect(open_google)
        layout.addWidget(button1, 1, 0)

        button2= QPushButton("Youtube")
        button2.setFixedSize(160, 60)
        def open_youtube():
            webbrowser.open('http://www.youtube.com')
        button2.clicked.connect(open_youtube)
        layout.addWidget(button2, 1, 1)

        button3= QPushButton("Facebook")
        button3.setFixedSize(160, 60)
        def open_facebook():
            webbrowser.open('http://www.facebook.com')
        button3.clicked.connect(open_facebook)
        layout.addWidget(button3, 1, 2)

        self.shortcut_open = QShortcut(QKeySequence("Ctrl+C"), self)
        self.shortcut_open.activated.connect(QApplication.quit)

        self.weather()

    def weather(self):
        ip = requests.get("https://api.ipify.org").text
        location = requests.get(f"http://ip-api.com/json/{ip}").json()
        city = location["city"]
        api = "76f134e6a027035aa096a05b3f360019"
        weather = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api}&units=metric").json()
        temp = weather["main"]["temp"]
        self.weather_label = QLabel(f"The temperature in {city} is {temp}°C")
        self.weather_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.weather_label.setStyleSheet("color: white; font-size: 30px;")
        self.layout().addWidget(self.weather_label, 0, 0, 1, 3)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background)