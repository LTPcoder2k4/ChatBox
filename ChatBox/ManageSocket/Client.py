import socket


class Client:
    def __init__(self):
        SERVER = "13.59.15.185"
        PORT = 16533
        ADDR = (SERVER, PORT)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)

        self.LIMIT = 64
        self.FORMAT = 'utf-8'

    def send(self, msg):
        message = msg.encode(self.FORMAT)
        self.client.send(message)

    def receive(self):
        msg = self.client.recv(self.LIMIT).decode(self.FORMAT)
        if msg != None or msg != '': #Check if message not empty
            return msg


if __name__ == "__main__":
    print('Please open main.py')
