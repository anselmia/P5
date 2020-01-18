from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        self.master = master
        self.root = Tk(master)

        self.widgets = {
            "substitute_button" : Button(self.root, text="Substituer un aliment", command=substitute),
            "text_interface" : Text(self.root,state=DISABLED)
        }

        self.send_text_in_interface(self.widgets["text_interface"], "Bienvenue")
        self.pack(self.widgets)
        self.root.mainloop()

    def substitute(self):
        pass

    def pack(widgets):
        for widget in widgets.values():
            widget.pack() 

    def send_text_in_interface(text_widget, text):
        widget.configure(state='normal')
        widget.insert('end', text)
        widget.configure(state='disabled')









