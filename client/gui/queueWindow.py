#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget

from ..communication.access import join

class QueueWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init()

    def init(self):
        join(False)
        self.setGeometry(700, 400, 400, 200)
        self.setWindowTitle("Szachy kolejka")
        self.show()