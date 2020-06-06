#!/usr/bin/python3

import threading

from .queueWindow import QueueWindow
from .gameWindow import GameWindow

from ..communication.access import connect, join, listen, check_av_moves, move

def connect1(server, port):
    connect(server, port)

def listenThread3():
    listen()

def listen1():
    listenThread = threading.Thread(target=listenThread3)
    listenThread.start()

def join1(bot):
    join(bot)

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

def check_av_moves1(piece):
    check_av_moves(piece)