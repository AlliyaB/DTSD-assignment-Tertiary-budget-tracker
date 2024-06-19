# Import tkinter.
import tkinter as tk
from tkinter import  *
from tkinter.ttk import *

signup_window = Tk()
signup_window.geometry("300x350")
canvas = Canvas(signup_window, height = 50, width = 350, bg = "CadetBlue2", )
canvas.place(x = 0, y = 20)
subtitle_lbl = Label(signup_window, text = "Create an account ").grid(row = 0)
firstname_lbl = Label(signup_window, text='First Name:').grid(row=1)
lastname_lbl = Label(signup_window, text='Last Name:').grid(row=2)
password_lbl = Label(signup_window, text='Create Password:').grid(row=4)
confirmpassword_lbl = Label(signup_window, text='Confirm Password:').grid(row=6)
e1 = Entry(signup_window)
e2 = Entry(signup_window)
e4 = Entry(signup_window)
e6 = Entry(signup_window)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e4.grid(row=4, column=1)
e6.grid(row=6, column=1)
mainloop()