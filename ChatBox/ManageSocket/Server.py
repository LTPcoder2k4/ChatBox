import socket
import threading


class Server:
    def __init__(self, app, db):
        PORT = 5050
        SERVER = "192.168.1.8"
        ADDR = (SERVER, PORT)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)

        self.LIMIT = 2048
        self.FORMAT = 'utf-8'
        self.list_connected = []
        self.app = app
        self.app.master.title(SERVER)
        self.db = db

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
                try:
                    message = msg.encode(self.FORMAT)
                    c.send(message)
                except:
                    self.list_connected.remove(conn)

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

        self.app.update_msg(f"[NEW CONNECTION] {name} connected.")
        self.db.push_data(f"[NEW CONNECTION] {name} connected.")
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
                self.app.update_msg(msg)
                self.db.push_data(msg)
                #Send message to others connection
                self.announce(conn, msg)

        conn.close()
        self.list_connected.remove(conn)
        self.app.update_msg(f"[DISCONNECTION] {name} disconected.")
        self.db.push_data(f"[DISCONNECTION] {name} disconected.")
        self.announce(conn, f"[DISCONNECTION] {name} disconected.")

    def start(self):
        self.app.update_msg("[STARTING] Server is starting...")
        self.app.update_msg(self.db.query())
        self.server.listen()
        while True:
            conn, addr = self.server.accept()
            self.list_connected.append(conn)
            thread = threading.Thread(target=self.handle_client, args=(conn,))
            thread.start()


if __name__ == "__main__":
    print("Please open admin.py")
