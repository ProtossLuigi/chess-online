#!/usr/bin/python3

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton

from .queueWindow import QueueWindow
from .gameWindow import GameWindow

class MenuWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init()

    def init(self):
        startComputerButton = QPushButton("&Gra z komputerem", self)
        startComputerButton.clicked.connect(self.startComputer)
        startOnlineButton = QPushButton("&Gra online", self)
        startOnlineButton.clicked.connect(self.startOnline)
        exitButton = QPushButton("&Powrót", self)
        exitButton.clicked.connect(self.finish)

        columnLayout = QGridLayout()
        columnLayout.addWidget(startComputerButton)
        columnLayout.addWidget(startOnlineButton)
        columnLayout.addWidget(exitButton)

        self.setLayout(columnLayout)
        self.setGeometry(700, 400, 400, 160)
        self.setWindowTitle("Szachy")
        self.show()

    def startComputer(self):
        from .globals import join1
        join1(True)

    def startOnline(self):
        from .globals import queueWindowShow
        from .globals import join1
        join1(False)
        queueWindowShow()

    def finish(self):
        self.close()