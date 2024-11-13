from tkinter import *

window = Tk()

window.geometry("640x480")

icon = PhotoImage(file="crown.png")
window.iconphoto(True, icon)

title = window.title("Menu GUI")

menu = Label(text="Menu",font="Sans-Serif",foreground="#33B9FF")
menu.pack()

window.mainloop()
