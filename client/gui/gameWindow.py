#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QMainWindow, QGraphicsScene, QGraphicsView, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QBoxLayout, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QPainter, QPen, QBrush, QFont
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore

from .boardWidget import BoardWidget

class GameWindow(QMainWindow):

    display_update = QtCore.pyqtSignal()

    def window_update(self):
        self.repaint()

    def __init__(self, color, parent=None):
        super().__init__(parent)
        self.color = color
        self.init()
        self.display_update.connect(self.window_update)

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

        self.margin = QLabel("", self)
        self.margin.setMargin(20)
        columnLayout.addWidget(self.margin)

        turlTitleLabel = QLabel("Aktulnie gra: ", self)
        turlTitleLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        turlTitleLabel.setAlignment(Qt.AlignCenter)
        turlTitleLabel.setFont(QFont('Arial', 16))
        columnLayout.addWidget(turlTitleLabel)

        self.turnLabel = QLabel("", self)
        self.turnLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.turnLabel.setAlignment(Qt.AlignCenter)
        self.turnLabel.setFont(QFont('Arial', 14))
        columnLayout.addWidget(self.turnLabel)

        self.queen = QPushButton("&queen", self)
        self.queen.clicked.connect(self.queen1)
        columnLayout.addWidget(self.queen)
        self.rook = QPushButton("&rook", self)
        self.rook.clicked.connect(self.rook1)
        columnLayout.addWidget(self.rook)
        self.bishop = QPushButton("&bishop", self)
        self.bishop.clicked.connect(self.bishop1)
        columnLayout.addWidget(self.bishop)
        self.knight = QPushButton("&knight", self)
        self.knight.clicked.connect(self.knight1)
        columnLayout.addWidget(self.knight)

        self.margin2 = QLabel("", self)
        self.margin2.setMargin(20)
        columnLayout.addWidget(self.margin2)
        
        self.checkLabel = QLabel("", self)
        self.checkLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.checkLabel.setAlignment(Qt.AlignCenter)
        self.checkLabel.setFont(QFont('Arial', 18))
        self.checkLabel.setStyleSheet('color: red')
        columnLayout.addWidget(self.checkLabel)

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
        self.checkLabel.setText("")
        self.display_update.emit()

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

    def update_board(self, moves, piece):
        self.boardWidget.update_board(moves, piece)

    def promote_pawn(self, x, y):
        pass

    def queen1(self):
        from .globals import promote1
        promote1("queen")
        self.boardWidget.promote_pawn(0, 0)

    def rook1(self):
        from .globals import promote1
        promote1("rook")
        self.boardWidget.promote_pawn(0, 0)

    def bishop1(self):
        from .globals import promote1
        promote1("bishop")
        self.boardWidget.promote_pawn(0, 0)

    def knight1(self):
        from .globals import promote1
        promote1("knight")
        self.boardWidget.promote_pawn(0, 0)

    def victory(self):
        self.checkLabel.setText("Zwycięstwo!!")
        self.checkLabel.setStyleSheet('color: green')
        self.display_update.emit()

    def defeat(self):
        self.checkLabel.setText("Przegrana!!")
        self.checkLabel.setStyleSheet('color: red')
        self.display_update.emit()

    def draw(self):
        self.checkLabel.setText("Remis!!")
        self.checkLabel.setStyleSheet('color: black')
        self.display_update.emit()

    def check(self):
        self.checkLabel.setStyleSheet('color: blue')
        self.checkLabel.setText("Masz szacha, ratuj króla")
        self.display_update.emit()