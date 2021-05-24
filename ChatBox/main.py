from ManageSocket import Client
from Gui import Take_name
from Database import Db

if __name__ == "__main__":
    try:
        root = Take_name.Tk()
        client = Client.Client()
        db = Db.Database()
        app = Take_name.Window(root, client, db)
        app.name_gui()
        root.mainloop()
    except:
        print('Server is not being connected!')
