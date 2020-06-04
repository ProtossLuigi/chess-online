#!/usr/bin/python3

import sys

from PyQt5.QtWidgets import QApplication
from .startWindow import StartWindow

app = QApplication(sys.argv)
window = StartWindow()
sys.exit(app.exec_())