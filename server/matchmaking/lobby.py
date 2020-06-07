import threading
from queue import Queue
from random import shuffle

from server.bot.learning_bot import TrainedBot
from server.game_logic.board import Game


class Lobby:
    lobby_lock = threading.Lock()
    waitroom = Queue()


def join(player, bot):
    Lobby.lobby_lock.acquire()
    if bot:
        players = [TrainedBot(), player]
        shuffle(players)
        Game(players[0], players[1])
    elif Lobby.waitroom.empty():
        Lobby.waitroom.put_nowait(player)
    else:
        players = [Lobby.waitroom.get_nowait(), player]
        shuffle(players)
        Game(players[0], players[1])
    Lobby.lobby_lock.release()
