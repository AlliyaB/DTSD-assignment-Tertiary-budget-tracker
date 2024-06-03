import tkinter as tk

#print label
from tkinter import *
root = Tk()
w = Label(root, text='Tertiary budget tracker!', width = 40, height = 10)
w.pack()
root.mainloop()

# Ask user name
from tkinter import *

window = Tk()
window.geometry("300x300")
lbl = Label(master = window, text = "Create an account ").grid(row = 0)
Label(master = window, text='First Name:').grid(row=1)
Label(master = window, text='Last Name:').grid(row=2)
Label(master = window, text='Create Password:').grid(row=4)
e1 = Entry(master = window)
e2 = Entry(master = window)
e4 = Entry(master = window)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e4.grid(row=4, column=1)
mainloop()