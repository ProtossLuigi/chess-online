#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QMainWindow, QGraphicsScene, QGraphicsView, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QBoxLayout, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPainter, QPen, QBrush, QFont
from PyQt5.QtCore import QRect, Qt

from .boardWidget import BoardWidget

class GameWindow(QMainWindow):

    #display_update = QtCore.pyqtSignal()

    # def window_update(self):
    #     print(threading.main_thread().ident)
    #     print(threading.current_thread().ident)
    #     self.repaint()

    def __init__(self, color, parent=None):
        super().__init__(parent)
        self.color = color
        self.init()
       # self.display_update.connect(self.window_update)

    def init(self):
        rowLayout = QHBoxLayout()

        self.boardWidget = BoardWidget(self.color)
        rowLayout.addWidget(self.boardWidget)

        columnLayout = QVBoxLayout()
        columnLayout.setContentsMargins(0, 6, 0, 0)
        columnLayout.setSpacing(0)
        columnLayout.setAlignment(Qt.AlignTop)
        
        whoAreYouTitleLabel = QLabel("Grasz jako: ", self)
        whoAreYouTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        whoAreYouTitleLabel.setAlignment(Qt.AlignCenter)
        whoAreYouTitleLabel.setFont(QFont('Arial', 16))
        columnLayout.addWidget(whoAreYouTitleLabel)

        self.whoAreYouTitleLabel = QLabel(self.color, self)
        self.whoAreYouTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.whoAreYouTitleLabel.setAlignment(Qt.AlignCenter)
        self.whoAreYouTitleLabel.setFont(QFont('Arial', 14))
        columnLayout.addWidget(self.whoAreYouTitleLabel)

        turlTitleLabel = QLabel("Aktulnie gra: ", self)
        turlTitleLabel.setContentsMargins(0, 40, 0, 0)
        turlTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        turlTitleLabel.setAlignment(Qt.AlignCenter)
        turlTitleLabel.setFont(QFont('Arial', 16))
        columnLayout.addWidget(turlTitleLabel)

        self.turnLabel = QLabel("", self)
        self.turnLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.turnLabel.setAlignment(Qt.AlignCenter)
        self.turnLabel.setFont(QFont('Arial', 14))
        columnLayout.addWidget(self.turnLabel)

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
    
    def showTurn(self, your):
        if (your and self.color == "Bialy"):
            self.turnLabel.setText("Bialy")
        if (your and self.color == "Czarny"):
            self.turnLabel.setText("Czarny")
        if (not your and self.color == "Bialy"):
            self.turnLabel.setText("Czarny")
        if (not your and self.color == "Czarny"):
            self.turnLabel.setText("Bialy")
       # self.re

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QBrush(Qt.white, Qt.SolidPattern))
   
    def your_turn(self):
        self.showTurn(True)
        self.boardWidget.your_turn()
    
    def opponent_turn(self):
        self.showTurn(False)
        self.boardWidget.opponent_turn()

    def available_moves(self, moves):
        self.boardWidget.available_moves(moves)

    def update_board(self, moves, piece):
        self.boardWidget.update_board(moves, piece)