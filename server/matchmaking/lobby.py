import threading
from queue import Queue


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
        pass
    Lobby.lobby_lock.release()
