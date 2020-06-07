#!/usr/bin/python3

import threading

from .queueWindow import QueueWindow
from .gameWindow import GameWindow
from .menuWindow import MenuWindow

from ..communication.access import connect, join, listen, check_av_moves, move, promote

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
    global menuWindow
    menuWindow = MenuWindow()
    menuWindow.show()

def queueWindowShow():
    global queueWindow
    queueWindow = QueueWindow()
    queueWindow.show()
    queueWindow.close()

def gameWindowShow(color):
    global gameWindow
    gameWindow = GameWindow(color)
    gameWindow.show()
    queueWindow.close()

def your_turn1():
    gameWindow.your_turn()

def opponent_turn1():
    gameWindow.opponent_turn()

def available_squares1(moves):
    gameWindow.available_moves(moves)

def update_board1(moves, piece):
    gameWindow.update_board(moves, piece)

def promote_pawn1(x, y):
    self.promote1("queen")

######

def check_av_moves1(piece):
    check_av_moves(piece)

def move1(dst):
    move(dst)

def promote1(name):
    print(name)
    promote(name)