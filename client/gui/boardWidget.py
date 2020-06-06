#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QGraphicsScene
from PyQt5.QtGui import QPalette, QColor, QPainter, QPen, QBrush, QPixmap, QCursor
from PyQt5.QtCore import QRect, Qt, QPoint

from .boardConfig import BoardConfig as boardConfig

from ..communication.access import check_av_moves, move

class BoardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
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
        
        if (len(self.availableMoves) > 0 and self.moveDone):
            previous_x = self.currentMouse["y"]
            previous_y = self.currentMouse["x"]
            for available in self.availableMoves:
                if (available["chosen"]):
                    next_x = available["y"]
                    next_y = available["x"]
                    previous = self.boardView[previous_x][previous_y]
                    previous_value = previous["iconContainer"]["value"]
                    self.boardView[next_x][next_y]["iconContainer"]["value"] = previous_value
                    self.boardView[previous_x][previous_y]["iconContainer"]["value"] = boardConfig.nothing()
                    self.availableMoves = []
                    break

        if (self.currentMouse != None):
            if (self.moveStarted != None and self.moveStarted["started"] == "no"):
                painter.setOpacity(0)
                rect = self.currentMouse["rect"]
                painter.fillRect(rect["position"], rect["brush"])
                self.calculateMouseEvent(self.rightPressedPosition)
                self.moveStarted = {
                    "started": "not_yet"
                }
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
                # print(self.currentMouse["x"])
                # print(self.currentMouse["y"])

    def mousePressEvent(self, e):
        if (self.your_turn):
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
                        self.moveDone = True
                        self.availableMoves[i]["chosen"] = True
                        self.moveStarted = {
                            "started": "no"
                        }
                        self.rightPressedPosition = e.pos()
                        self.update()
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
                                    check_av_moves((x, y))
                                   
            elif e.button() == Qt.RightButton:
                self.moveStarted = {
                    "started": "no"
                }
                self.rightPressedPosition = e.pos()
                self.update()
    
    def mouseMoveEvent(self, e):
        if (self.your_turn):
            if (self.moveStarted != None and self.moveStarted["started"] == "yes"):
                return

            pos = e.pos()
            self.calculateMouseEvent(pos)
    
    def calculateMouseEvent(self, pos):
        if (self.your_turn):
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
                                self.update()
                                return
                            else:
                                if (self.currentMouse["x"] != x or self.currentMouse["y"] != y):
                                    self.currentMouse = newCurrentMouse
                                    self.update()
                                    return

    def your_turn():
        self.your_turn = True

    def opponent_turn():
        self.your_turn = False

    def available_squares(squares):
        self.moveDone = False
        self.availableMoves = []
        for piece in squares:
            availableMoves.append({ "x": piece[0], piece[1], "chosen": False })
            self.moveStarted = {
                "started": "yes"
            }
            self.update()
            break