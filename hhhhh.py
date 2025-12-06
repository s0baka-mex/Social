from tkinter import *
from tkinter import ttk, messagebox, Canvas
win = Tk()
win.title("title")
win.config(cursor="hand2")
win_m = Menu()
def commande():
    a=Label(win, text="""from tkinter import *
from tkinter import ttk, messagebox, Canvas
win = Tk()
win.title("title")
win.config(cursor="hand2")
win_m = Menu()
def commande():
    a=Label(win, text="""""")
win_m.add_command(label='Code of page', command=commande)""").pack()
win_m.add_command(label='Code of page', command=commande)
win.config(menu=win_m)
mainloop()