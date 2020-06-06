#!/usr/bin/python3

from .queueWindow import QueueWindow
from .gameWindow import GameWindow

def initialization():
    global queueWindow
    queueWindow = QueueWindow()
    queueWindow.show()

def gameWindowShow(color):
    global gameWindow
    gameWindow = GameWindow(color)
    gameWindow.show()

def your_turn1():
    gameWindow.your_turn()

def opponent_turn1():
    gameWindow.opponent_turn()