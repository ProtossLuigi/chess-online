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
            [ Rook("Czarny"), Knight("Czarny"), Bishop("Czarny"), Queen("Czarny"), King("Czarny"), Bishop("Czarny"), Knight("Czarny"), Rook("Czarny") ],
            [ Pawn("Czarny"), Pawn("Czarny"), Pawn("Czarny"), Pawn("Czarny"), Pawn("Czarny"), Pawn("Czarny"), Pawn("Czarny"), Pawn("Czarny") ],
            [ Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing("") ],
            [ Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing("") ],
            [ Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing("") ],
            [ Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing(""), Nothing("") ],
            [ Pawn("Bialy"), Pawn("Bialy"), Pawn("Bialy"), Pawn("Bialy"), Pawn("Bialy"), Pawn("Bialy"), Pawn("Bialy"), Pawn("Bialy") ],
            [ Rook("Bialy"), Knight("Bialy"), Bishop("Bialy"), Queen("Bialy"), King("Bialy"), Bishop("Bialy"), Knight("Bialy"), Rook("Bialy") ]
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

    def queen(color):
        return Queen(color)

class Type:
    def __init__(self, name, color, iconBialy, iconCzarny, left, top):
        if (color == "Bialy"):
            self.icon = QPixmap(iconBialy)
        elif (color == "Czarny"):
            self.icon = QPixmap(iconCzarny)
        else:
            self.icon = None

        self.name = name
        self.top = top
        self.left = left
        self.color = color
        
    def getIcon(self):
        return self.icon

    def marginTop(self):
        return self.top

    def marginLeft(self):
        return self.left

    def getColor(self):
        return self.color

    def getName(self):
        return self.name
    
class King(Type):
    def __init__(self, color):
        Type.__init__(self, "king", color, "./client/gui/images/king_white.png", "./client/gui/images/king.png", 24, 8)

class Queen(Type):
    def __init__(self, color):
        Type.__init__(self, "queen", color, "./client/gui/images/queen_white.png", "./client/gui/images/queen.png", 24, 8)

class Rook(Type):
    def __init__(self, color):
        Type.__init__(self, "rook", color, "./client/gui/images/rook_white.png", "./client/gui/images/rook.png", 22, 8)

class Knight(Type):
    def __init__(self, color):
        Type.__init__(self, "knight", color, "./client/gui/images/knight_white.png", "./client/gui/images/knight.png", 20, 8)

class Bishop(Type):
    def __init__(self, color):
        Type.__init__(self, "bishop", color, "./client/gui/images/bishop_white.png", "./client/gui/images/bishop.png", 24, 8)

class Pawn(Type):
    def __init__(self, color):
        Type.__init__(self, "pawn", color, "./client/gui/images/pawn_white.png", "./client/gui/images/pawn.png", 20, 8)

class Nothing(Type):
    def __init__(self, color):
        Type.__init__(self, "nothing", color, "", "", 0, 0)
