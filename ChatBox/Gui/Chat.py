from tkinter import*
from tkinter import messagebox
import threading


class Window(Frame):
    def __init__(self, master, client, name):
        Frame.__init__(self, master)
        self.master = master
        self.name = name
        self.MessageInput = Entry()
        self.client = client
        self.master.title("App Chat - " + self.name)

    def send_msg(self):
        msg = self.MessageInput.get()
        if len(msg) > 0:
            try:
                self.txtMessage.insert(END, "\n" + "[You]: " + msg)
                self.txtMessage.see(END)
                self.client.send(msg)
                self.MessageInput.delete(0, END)
            except:
                messagebox.showerror("Error", "You are disconnected")
                return

    def receive_msg(self):
        while True:
            try:
                msg = self.client.receive()
                self.txtMessage.insert(END, "\n" + msg)
                self.txtMessage.see(END)
            except:
                messagebox.showerror("Error", "You are disconnected")
                break

    def chat_gui(self):
        self.txtMessage = Text(self.master, width=50)
        self.txtMessage.grid(row=0, column=0, padx=10, pady=10)

        self.MessageInput = Entry(self.master, width=50)
        self.MessageInput.insert(0, "Your message")
        self.MessageInput.grid(row=1, column=0, padx=10, pady=10)

        btnSendMessage = Button(self.master, text="Send", width=20, command=self.send_msg)
        btnSendMessage.grid(row=2, column=0, padx=10, pady=10)

        thread = threading.Thread(target=self.receive_msg)
        thread.daemon = True
        thread.start()

        self.master.mainloop()

