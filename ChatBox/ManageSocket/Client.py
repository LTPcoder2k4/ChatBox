import socket


class Client:
    def __init__(self):
        SERVER = "192.168.1.8"
        PORT = 5050
        ADDR = (SERVER, PORT)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)

        self.LIMIT = 2048
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
