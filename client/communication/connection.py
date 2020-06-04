from client.communication.message_encoder import to_json


def send(socket, msg):
    json = to_json(msg)
    socket.send(json)
