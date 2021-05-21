import socket
import threading


class Server:
    def __init__(self):
        PORT = 5050
        SERVER = "127.0.0.1"
        ADDR = (SERVER, PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)

        self.LIMIT = 64
        self.FORMAT = 'utf-8'
        self.list_connected = []

    def take_name(self, conn):
        get_name = False
        while not get_name:
            msg = conn.recv(self.LIMIT).decode(self.FORMAT)
            if len(msg) > 0:  # Check if message not empty
                return msg

    def optimize(self, txt):
        while txt[0] == ' ' and len(txt) > 0:
            txt = txt[1::]
        while txt[-1] == ' ' and len(txt) > 0:
            txt = txt[:-1]
        return txt

    def announce(self, conn, msg):
        for c in self.list_connected:
            if c != conn:
                message = msg.encode(self.FORMAT)
                c.send(message)

    def handle_client(self, conn):
        name = self.take_name(conn)

        if len(name) > 0:
            name = self.optimize(name)
        else:#if client disconnect while get name
            conn.close()
            try:
                self.list_connected.remove(conn)
            except:
                pass
            return

        print(f"[NEW CONNECTION] {name} connected.")
        self.announce(conn, f"[NEW CONNECTION] {name} connected.")

        connected = True
        while connected:
            #Receive message
            try:
                msg = self.optimize(conn.recv(self.LIMIT).decode(self.FORMAT))
            except: #client is disconected
                break

            if len(msg) > 0:
                msg = f"[{name}]: {msg}"
                print(msg)
                #Send message to others connection
                self.announce(conn, msg)

        conn.close()
        self.list_connected.remove(conn)
        print(f"[DISCONNECTION] {name} disconected.")
        self.announce(conn, f"[DISCONNECTION] {name} disconected.")

    def start(self):
        print("[STARTING] Server is starting...")
        self.server.listen()
        while True:
            conn, addr = self.server.accept()
            self.list_connected.append(conn)
            thread = threading.Thread(target=self.handle_client, args=(conn,))
            thread.start()


if __name__ == "__main__":
    run = Server()
    run.start()
