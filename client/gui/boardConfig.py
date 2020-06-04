#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QGraphicsScene
from PyQt5.QtGui import QPalette, QColor, QBrush, QPixmap
from PyQt5.QtCore import Qt

standardBoardSize = 8
legendSize = 1

class BoardConfig():
    
    def boardSize():
        return standardBoardSize + legendSize, standardBoardSize + legendSize

    def legend():
        return {
            "row": [ "A", "B", "C", "D", "E", "F", "G", "H" ],
            "column": [ "8", "7", "6", "5", "4", "3", "2", "1" ]
        }

    def legendLong():
        return 75
    
    def legendShort():
        return 37.5

    def startBoard():
        return [
            [ Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black") ],
            [ Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black") ],
            [ Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing("") ],
            [ Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing("") ],
            [ Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing("") ],
            [ Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing("") ],
            [ Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white") ],
            [ Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white") ]
        ]

    def rectSize():
        return 75

    def brushLegend():
        return QBrush(Qt.white, Qt.SolidPattern)
    
    def brushBrown():
        return QBrush(QColor(122, 62, 34), Qt.SolidPattern)
    
    def brushWhite():
        return QBrush(QColor(167, 135, 78), Qt.SolidPattern)

    def brushMouseMove():
        return QBrush(QColor(134, 155, 113), Qt.SolidPattern)
    
    def nothing():
        return Nothing("")

class Type:
    def __init__(self, name, color, iconWhite, iconBlack, left, top):
        if (color == "white"):
            self.icon = QPixmap(iconWhite)
        elif (color == "black"):
            self.icon = QPixmap(iconBlack)
        else:
            self.icon = None

        self.name = name
        self.top = top
        self.left = left
        
    def getIcon(self):
        return self.icon

    def marginTop(self):
        return self.top

    def marginLeft(self):
        return self.left

    def getName(self):
        return self.name
    
class King(Type):
    def __init__(self, color):
        Type.__init__(self, "king", color, "./images/king_white.png", "./images/king.png", 24, 8)

class Queen(Type):
    def __init__(self, color):
        Type.__init__(self, "queen", color, "./images/queen_white.png", "./images/queen.png", 24, 8)

class Rook(Type):
    def __init__(self, color):
        Type.__init__(self, "rook", color, "./images/rook_white.png", "./images/rook.png", 22, 8)

class Knight(Type):
    def __init__(self, color):
        Type.__init__(self, "knight", color, "./images/knight_white.png", "./images/knight.png", 20, 8)

class Bishop(Type):
    def __init__(self, color):
        Type.__init__(self, "bishop", color, "./images/bishop_white.png", "./images/bishop.png", 24, 8)

class Pawn(Type):
    def __init__(self, color):
        Type.__init__(self, "pawn", color, "./images/pawn_white.png", "./images/pawn.png", 20, 8)

class Nothing(Type):
    def __init__(self, color):
        Type.__init__(self, "nothing", color, "", "", 0, 0)