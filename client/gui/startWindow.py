#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QHBoxLayout, QPushButton, QLineEdit

import threading

from .menuWindow import MenuWindow
from .queueWindow import QueueWindow
from ..communication.access import connect, listen

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

    
    def listenThread(self):
        listen()

    def start(self):
        try:
            connect('127.0.1.1', 38363)
            listenThread = threading.Thread(target=self.listenThread)
            listenThread.start()
            self.queueWindow = QueueWindow()
            self.queueWindow.show()
        except:
            print("INTERNAL PROBLEM")
        
      
    def exit(self):
        self.close()