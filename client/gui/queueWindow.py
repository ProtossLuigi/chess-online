#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QMainWindow

from .gameWindow import GameWindow

class QueueWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init()

    def init(self):
        self.setGeometry(700, 400, 400, 200)
        self.setWindowTitle("Szachy kolejka")
        self.show()

    def game_start(color):
        gameWindow = GameWindow(color)
        gameWindow.show()
