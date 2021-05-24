from ManageSocket import Server
from Gui import Admin
from Database import Db
import threading


def sv(server):
    server.start()


if __name__ == "__main__":
    try:
        root = Admin.Tk()
        db = Db.Database()
        app = Admin.Window(root, db)
        server = Server.Server(app, db)
        thread1 = threading.Thread(target=sv, args=(server,))
        thread1.start()
        root.mainloop()
    except:
        print("Can't create server!")
