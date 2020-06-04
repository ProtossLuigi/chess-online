#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QMainWindow, QGraphicsScene, QGraphicsView, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QBoxLayout, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPainter, QPen, QBrush, QFont
from PyQt5.QtCore import QRect, Qt

from boardWidget import BoardWidget

class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init()

    def init(self):
        rowLayout = QHBoxLayout()

        boardWidget = BoardWidget(self)
        rowLayout.addWidget(boardWidget)

        columnLayout = QVBoxLayout()
        columnLayout.setContentsMargins(0, 6, 0, 0)
        columnLayout.setSpacing(0)
        columnLayout.setAlignment(Qt.AlignTop)
        
        whoAreYouTitleLabel = QLabel("Grasz jako: ", self)
        whoAreYouTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        whoAreYouTitleLabel.setAlignment(Qt.AlignCenter)
        whoAreYouTitleLabel.setFont(QFont('Arial', 16))
        columnLayout.addWidget(whoAreYouTitleLabel)

        self.whoAreYouTitleLabel = QLabel("Biały", self)
        self.whoAreYouTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.whoAreYouTitleLabel.setAlignment(Qt.AlignCenter)
        self.whoAreYouTitleLabel.setFont(QFont('Arial', 14))
        columnLayout.addWidget(self.whoAreYouTitleLabel)

        widgetColumn = QWidget()
        widgetColumn.setLayout(columnLayout)
        widgetColumn.setStyleSheet("background-color:lightGray;")
        rowLayout.addWidget(widgetColumn)

        widget = QWidget()
        widget.setLayout(rowLayout)
        self.setCentralWidget(widget)
        self.setGeometry(400, 200, 1200, 800)
        self.setFixedSize(1200, 659)
        self.setWindowTitle("Szachy gra - komputer")
        self.show()
    
    def paintEvent(self, e):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QBrush(Qt.white, Qt.SolidPattern))
   