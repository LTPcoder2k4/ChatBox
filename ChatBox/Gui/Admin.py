from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext


class Window:
    def __init__(self, master, db):
        self.master = master
        self.master.iconbitmap("./img/logo-admin.ico")
        self.db = db
        self.admin_gui()

    def clear_all(self):
        self.db.delete_data()
        self.txtMsg.configure(state='normal')
        self.txtMsg.delete('0.0', END)
        self.txtMsg.configure(state='disable')

    def alert(self, err):
        messagebox.showerror("Error", err)

    def update_msg(self, msg):
        self.txtMsg.configure(state='normal')
        self.txtMsg.insert(END, "\n" + str(msg))
        self.txtMsg.configure(state='disable')
        self.txtMsg.see(END)

    def admin_gui(self):
        self.txtMsg = scrolledtext.ScrolledText(self.master, width=50)
        self.txtMsg.grid(row=0, column=0, padx=10, pady=10)
        clrall = Button(self.master, text="Clear all message", command=self.clear_all)
        clrall.grid(row=0, column=1, padx=10, pady=10)
