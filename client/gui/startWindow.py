#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QPushButton, QLineEdit

from .globals import initialization, connect1, join1, listen1

class StartWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init()

    def init(self):
        layout = QGridLayout()
        layout.addWidget(QLabel("Witamy w grze szachy. By zacząć uzupełnij pola:", self), 0, 0)
        layout.addWidget(QLabel("Server", self), 1, 0)
        layout.addWidget(QLabel("Port", self), 1, 1)
        self.serverView = QLineEdit()
        self.portView = QLineEdit()

        layout.addWidget(self.serverView, 2, 0)
        layout.addWidget(self.portView, 2, 1)

        startButton = QPushButton("&Start", self)
        startButton.clicked.connect(self.start)

        layout.addWidget(startButton, 3, 0, 1, 2)

        exitButton = QPushButton("&Wyjście", self)
        exitButton.clicked.connect(self.exit)

        layout.addWidget(exitButton, 4, 0, 1, 2)

        self.setLayout(layout)
        self.setGeometry(700, 400, 400, 120)
        self.setWindowTitle("Szachy")
        self.show()
    
    def start(self):
        try:
            connect1('169.254.200.100', 52926)
            listen1()
            join1(False)
            initialization()
        except Exception as exception:
            print(f"StartWindow exception: {exception}")
           
    def exit(self):
        self.close()