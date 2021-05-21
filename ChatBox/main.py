from ManageSocket import Client
from Gui import Take_name

if __name__ == "__main__":
    try:
        root = Take_name.Tk()
        client = Client.Client()
        app = Take_name.Window(root, client)
        app.name_gui()
        root.mainloop()
    except:
        print('Server is not being connected!')
