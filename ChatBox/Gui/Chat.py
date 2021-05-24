from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
import threading


class Window(Frame):
    def __init__(self, master, client, name, db):
        Frame.__init__(self, master)
        self.master = master
        self.name = name
        self.MessageInput = Entry()
        self.client = client
        self.db = db
        self.master.title("App Chat - " + self.name)
        self.master.iconbitmap("./img/logo-app.ico")

    def update_msg(self, msg, ev=''):
        self.txtMsg.configure(state='normal')
        self.txtMsg.insert(END, "\n" + ev + str(msg))
        self.txtMsg.configure(state='disable')
        self.txtMsg.see(END)

    def send_msg(self, ev='0'):
        msg = self.MessageInput.get()
        if len(msg) > 0:
            try:
                self.update_msg(msg, "[You]: ")
                self.client.send(msg)
                self.MessageInput.delete(0, END)
            except:
                messagebox.showerror("Error", "You are disconnected")
                return

    def receive_msg(self):
        while True:
            try:
                msg = self.client.receive()
                self.update_msg(msg)
            except:
                messagebox.showerror("Error", "You are disconnected")
                break

    def load_history(self):
        self.update_msg(self.db.query())

    def chat_gui(self):
        self.txtMsg = scrolledtext.ScrolledText(self.master, width=50)
        self.txtMsg.configure(state='disable')
        self.load_history()
        self.txtMsg.grid(row=0, column=0, padx=10, pady=10)

        self.MessageInput = Entry(self.master, width=50)
        self.MessageInput.insert(0, "Your message")
        self.MessageInput.grid(row=1, column=0, padx=10, pady=10)

        btnSendMessage = Button(self.master, text="Send", width=20, command=self.send_msg)
        btnSendMessage.grid(row=2, column=0, padx=10, pady=10)
        self.master.bind("<Return>", self.send_msg)

        thread = threading.Thread(target=self.receive_msg)
        thread.daemon = True
        thread.start()

        self.master.mainloop()