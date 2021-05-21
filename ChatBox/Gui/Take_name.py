from tkinter import*
from Gui import Chat


class Window(Frame):
    def __init__(self, master, client):
        Frame.__init__(self, master)
        self.master = master
        self.name = ''
        self.inp = Entry()
        self.client = client
        self.master.title("Input your name")
        self.master.geometry("400x200")
        self.master.iconbitmap("./img/logo.ico")

    def change_window(self):
        tk = Tk()
        window = Chat.Window(tk, self.client, self.name)
        window.chat_gui()

    def return_name(self, ev='0'):
        self.name = self.inp.get()
        if len(self.name) > 0:
            self.client.send(self.name)
            self.master.destroy()
            self.change_window()

    def name_gui(self):
        lbl = Label(text="Your name: ", font=("Times New Roman", 30))
        self.inp = Entry(font=("Times New Roman", 30))
        btn = Button(text="Enter", height=5, width=30, font=("Times New Roman", 15), command=self.return_name)
        self.master.bind("<Return>", self.return_name)
        lbl.pack(fill=X)
        self.inp.pack()
        btn.pack()
