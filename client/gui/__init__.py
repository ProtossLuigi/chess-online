#!/usr/bin/python3

import sys

from PyQt5.QtWidgets import QApplication
from startWindow import StartWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StartWindow()
    sys.exit(app.exec_())