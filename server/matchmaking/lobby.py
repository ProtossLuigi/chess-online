import threading
from queue import Queue
from random import shuffle

from server.game_logic.board import Game


class Lobby:
    lobby_lock = threading.Lock()
    waitroom = Queue()


def join(player, bot):
    Lobby.lobby_lock.acquire()
    if bot:
        print('game vs bot NYI')
    elif Lobby.waitroom.empty():
        Lobby.waitroom.put(player)
    else:
        players = [Lobby.waitroom.get(), Lobby.waitroom.get()]
        shuffle(players)
        Game(players[0], players[1])
    Lobby.lobby_lock.release()
