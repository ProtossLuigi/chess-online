#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QGraphicsScene, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPalette, QColor, QPainter, QPen, QBrush, QPixmap, QCursor
from PyQt5.QtCore import QRect, Qt, QPoint
from PyQt5 import QtCore

from .boardConfig import BoardConfig as boardConfig

import threading

class BoardWidget(QWidget):

    def window_update(self):
        self.repaint()

    display_update = QtCore.pyqtSignal()

    def __init__(self, color, parent=None):
        super().__init__(parent)
        self.color = color
        self.init()

    def init(self):
        self.setFixedSize(637.5, 637.5)
        self.boardView = []
        self.createBoard()
        self.currentMouse = None
        self.moveStarted = {
            "started": "not_yet"
        }
        self.setMouseTracking(True)
        self.rightPressedPosition = None
        self.availableMoves = []
        self.display_update.connect(self.window_update)

    def createBoard(self):
        width, height = boardConfig.boardSize()
        boardItemsView = boardConfig.startBoard()
        legend = boardConfig.legend()

        brown = False
        brushLegend = boardConfig.brushLegend()
        brushBrown = boardConfig.brushBrown()
        brushWhite = boardConfig.brushWhite()
        i = 0
        while i < height:
            row = []
            j = 0
            while (j < width):
                item = {
                    "x": j,
                    "y": i,
                    "x_screen": None,
                    "y_screen": None,
                    "legend": True
                }

                if (i == 0 and j == 0):
                    item["iconContainer"] = None
                    item["rect"] = {
                        "position": QRect(j * boardConfig.legendShort(), i * boardConfig.legendShort(), boardConfig.legendShort(), boardConfig.legendShort()),
                        "brush": brushLegend
                    }
                elif (i == 0 and j > 0):
                    item["iconContainer"] = {
                        "position": QPoint(j * boardConfig.legendLong() - 5, (i+1) * boardConfig.legendShort() - 12),
                        "value": legend["row"][j - 1]
                    }
                    item["rect"] = {
                        "position": QRect(j * boardConfig.legendLong() - boardConfig.legendShort(), i * boardConfig.legendShort(), boardConfig.legendLong(), boardConfig.legendShort()),
                        "brush": brushLegend
                    }
                elif (i > 0 and j == 0):
                    item["iconContainer"] = {
                        "position": QPoint(j * boardConfig.legendShort() + 12, (i) * boardConfig.legendLong()),
                        "value": legend["column"][i - 1]
                    }
                    item["rect"] = {
                        "position": QRect(0, (i * boardConfig.legendLong()) - boardConfig.legendShort(), boardConfig.legendShort(), boardConfig.legendLong()),
                        "brush": brushLegend
                    }
                else:
                    item["legend"] = False
                    item["iconContainer"] = {
                        "position": QPoint(boardConfig.legendShort() + (j-1) * boardConfig.rectSize(), boardConfig.legendShort() + (i-1) * boardConfig.rectSize()),
                        "value": boardItemsView[i - 1][j - 1]
                    }
                    item["rect"] = {
                        "position": QRect(boardConfig.legendShort() + (j-1) * boardConfig.rectSize(), boardConfig.legendShort() + (i-1) * boardConfig.rectSize(), boardConfig.rectSize(), boardConfig.rectSize())
                    }
                    item["x_screen"] = boardConfig.legendShort() + (j-1) * boardConfig.rectSize()
                    item["y_screen"] = boardConfig.legendShort() + (i-1) * boardConfig.rectSize()

                    if (brown):
                        item["rect"]["brush"] = brushBrown
                    else:
                        item["rect"]["brush"] = brushWhite

                row.append(item)
                j += 1
                brown = not brown
            self.boardView.append(row)
            i += 1

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QBrush(Qt.white, Qt.SolidPattern))
        for column in self.boardView:
            for row in column:
                iconContainer = row["iconContainer"]
                if (iconContainer != None):
                    if (row["legend"]):
                        painter.drawText(iconContainer["position"], iconContainer["value"])
                    else:
                        rect = row["rect"]
                        painter.fillRect(rect["position"], rect["brush"])
                        value = iconContainer["value"]
                        view = value.getIcon()
                        if (view != None):
                            painter.drawPixmap(QPoint(iconContainer["position"].x() + value.marginLeft(), iconContainer["position"].y() + value.marginTop()), view) 
        
        # if (len(self.availableMoves) > 0 and self.moveDone):
        #     previous_x = self.currentMouse["y"]
        #     previous_y = self.currentMouse["x"]
        #     for available in self.availableMoves:
        #         if (available["chosen"]):
        #             next_x = available["y"]
        #             next_y = available["x"]
        #             previous = self.boardView[previous_x][previous_y]
        #             previous_value = previous["iconContainer"]["value"]
        #             # self.boardView[next_x][next_y]["iconContainer"]["value"] = previous_value
        #             # self.boardView[previous_x][previous_y]["iconContainer"]["value"] = boardConfig.nothing()
        #             self.availableMoves = []
        #             break

        if (self.currentMouse != None):
            if (self.moveStarted != None and self.moveStarted["started"] == "no"):
                painter.setOpacity(0)
                rect = self.currentMouse["rect"]
                painter.fillRect(rect["position"], rect["brush"])
                self.moveStarted = {
                    "started": "not_yet"
                }
                if (len(self.availableMoves) > 0):
                    for available in self.availableMoves:
                        rect = QRect(boardConfig.legendShort() + (available["x"]-1) * boardConfig.rectSize(), boardConfig.legendShort() + (available["y"]-1) * boardConfig.rectSize(), boardConfig.rectSize(), boardConfig.rectSize()) 
                        painter.fillRect(rect, boardConfig.brushMouseMove())        
            elif (self.moveStarted != None and self.moveStarted["started"] == "yes"):
                painter.setOpacity(0.6)
                rect = self.currentMouse["rect"]
                painter.fillRect(rect["position"], rect["brush"])
                if (len(self.availableMoves) > 0):
                    painter.setOpacity(0.6)
                    for available in self.availableMoves:
                        rect = QRect(boardConfig.legendShort() + (available["x"]-1) * boardConfig.rectSize(), boardConfig.legendShort() + (available["y"]-1) * boardConfig.rectSize(), boardConfig.rectSize(), boardConfig.rectSize()) 
                        painter.fillRect(rect, boardConfig.brushMouseMove())                  
            else:
                painter.setOpacity(0.6)
                rect = self.currentMouse["rect"]
                painter.fillRect(rect["position"], rect["brush"])

    def mousePressEvent(self, e):
        if (self.is_turn):
            from .globals import check_av_moves1, move1
            pos = e.pos()
            x = pos.x()
            y = pos.y()
            if e.button() == Qt.LeftButton:
                if (self.moveStarted["started"] == "yes"):
                    correctRect = False
                    i = 0
                    while i < len(self.availableMoves):
                        available = self.availableMoves[i]
                        if (x > boardConfig.legendShort() + (available["x"]-1) * boardConfig.rectSize() and 
                            x < boardConfig.rectSize() + boardConfig.legendShort() + (available["x"]-1) * boardConfig.rectSize() and 
                            y > boardConfig.legendShort() + (available["y"]-1) * boardConfig.rectSize() and 
                            y < boardConfig.rectSize() + boardConfig.legendShort() + (available["y"]-1) * boardConfig.rectSize() ):
                            correctRect = True
                            break
                        i += 1
                    
                    if (correctRect):
                        move1((self.availableMoves[i]["y"] - 1, self.availableMoves[i]["x"] - 1))
                        #self.moveDone = True
                        self.availableMoves[i]["chosen"] = True
                        self.moveStarted = {
                            "started": "no"
                        }
                        # self.rightPressedPosition = e.pos()
                        self.availableMoves = []
                        self.currentMouse = None
                        self.display_update.emit()
                else:
                    for column in self.boardView:
                        for row in column:
                            if (x > boardConfig.legendShort() + (row["x"]-1) * boardConfig.rectSize() and 
                                x < boardConfig.rectSize() + boardConfig.legendShort() + (row["x"]-1) * boardConfig.rectSize() and 
                                y > boardConfig.legendShort() + (row["y"]-1) * boardConfig.rectSize() and 
                                y < boardConfig.rectSize() + boardConfig.legendShort() + (row["y"]-1) * boardConfig.rectSize() and
                                row["x"] > 0 and 
                                row["y"] > 0 and 
                                row["iconContainer"] != None 
                                and row["iconContainer"]["value"].getName() != "nothing"):
                                    if (row["iconContainer"]["value"].getColor() == self.color):
                                        check_av_moves1((row["y"]-1,row["x"]-1))
                                        #self.moveDone = False
                                        self.moveStarted = {
                                            "started": "yes"
                                        }
                                        self.display_update.emit()
                                        break
                                    
            elif e.button() == Qt.RightButton:
                self.moveStarted = {
                    "started": "no"
                }
                #self.rightPressedPosition = e.pos()
                self.repaint()
    
    # def leaveEvent(self, event):
    #     self.currentMouse = None
    #     self.display_update.emit()()
    
    def mouseMoveEvent(self, e):
        if (self.is_turn):
            if (self.moveStarted != None and self.moveStarted["started"] == "yes"):
                return

            pos = e.pos()
            self.calculateMouseEvent(pos)
    
    def calculateMouseEvent(self, pos):
        x = pos.x()
        y = pos.y()
        size = boardConfig.rectSize()
        if (self.currentMouse != None and x >= self.currentMouse["x_screen"] and x <= self.currentMouse["x_screen"] + size and y >= self.currentMouse["y_screen"] and y <= self.currentMouse["y_screen"] + size):
            return
        
        if (x > boardConfig.legendShort() and y > boardConfig.legendShort()):
            for column in self.boardView:
                for row in column:
                    x_screen = row["x_screen"]
                    y_screen = row["y_screen"]
                    if (x_screen != None and y_screen != None and x > x_screen and x < x_screen + size and y > y_screen and y < y_screen + size):
                        x = row["x"]
                        y = row["y"]
                        newCurrentMouse = {
                            "x": x,
                            "y": y,
                            "x_screen": x_screen,
                            "y_screen": y_screen,
                            "rect": {
                                "position": QRect(boardConfig.legendShort() + (x-1) * boardConfig.rectSize(), boardConfig.legendShort() + (y-1) * boardConfig.rectSize(), boardConfig.rectSize(), boardConfig.rectSize()),
                                "brush": boardConfig.brushMouseMove()
                            }
                        }

                        if (self.currentMouse == None):
                            self.currentMouse = newCurrentMouse
                            self.repaint()
                            return
                        else:
                            if (self.currentMouse["x"] != x or self.currentMouse["y"] != y):
                                self.currentMouse = newCurrentMouse
                                self.repaint()
                                return

    def your_turn(self):
        self.is_turn = True

    def opponent_turn(self):
        self.is_turn = False

    def available_moves(self, moves):
        self.availableMoves = []
        for move in moves:
            self.availableMoves.append({ "x": move[1] + 1, "y": move[0] + 1, "chosen": False })
        self.display_update.emit()

    def update_board(self, moves, piece):
        for move in moves:
            pieceFrom = move[0]
            pieceTo = move[1]

            previous = self.boardView[pieceFrom[0] + 1][pieceFrom[1] + 1]
            previous_value = previous["iconContainer"]["value"]
            if (previous_value.getName() != "nothing"):
                print(piece)
                print(isinstance(piece, str))
                if (isinstance(piece, str)):
                    if (self.is_turn and self.color == "Bialy"):
                        self.boardView[pieceTo[0] + 1][pieceTo[1] + 1]["iconContainer"]["value"] = boardConfig.queen("Bialy")
                    if (not self.is_turn and self.color == "Bialy"):
                        self.boardView[pieceTo[0] + 1][pieceTo[1] + 1]["iconContainer"]["value"] = boardConfig.queen("Czarny")
                    if (self.is_turn and self.color == "Czarny"):
                        self.boardView[pieceTo[0] + 1][pieceTo[1] + 1]["iconContainer"]["value"] = boardConfig.queen("Czarny")
                    if (not self.is_turn and self.color == "Czarny"):
                        self.boardView[pieceTo[0] + 1][pieceTo[1] + 1]["iconContainer"]["value"] = boardConfig.queen("Bialy")
                else:
                    self.boardView[pieceTo[0] + 1][pieceTo[1] + 1]["iconContainer"]["value"] = previous_value
                self.boardView[pieceFrom[0] + 1][pieceFrom[1] + 1]["iconContainer"]["value"] = boardConfig.nothing()
                self.display_update.emit()

    def promote_pawn(self, x, y):
        print("sdddd")
        pass
    
    # def show_promote_dialog(self):
    #     self.choosePawn = ChoosePawn()
    #     self.choosePawn.show()

    