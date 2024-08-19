# Import tkinter, date, and datetime.
import tkinter as tk
from tkinter import  *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image 
from datetime import datetime
from datetime import date

def popup():
    response = messagebox.askquestion("Exit Programme?","Your progress will " +
                                    "NOT be saved.\nAre you sure you want " +
                                    "to exit the program?", 
    icon = 'warning')
    print(response)
    if response == "yes":
        confirm_btn = Button(home_window, 
                            command = home_window.quit)
        confirm_btn.pack()
        home_window.destroy()

# Create Log in/sign up window.
home_window = tk.Tk()
home_window.geometry("1200x750")
home_window.title("Log in/Sign up")
home_window.resizable(False, False)

# Display label.
program_title = tk.Label(home_window,
    text = "Tertiary Budget \nTracker             ",
    font = ("Helvetica", 48))
program_title.place(x = 200, y = 250)

# Create window content for example labels and buttons.
canvas = Canvas(home_window, height = 100, width = 1210, bg = "CadetBlue2", )
exit = tk.Button(home_window,
                   text = "Exit",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "grey",
                   command = popup)
image = Image.open("Lean-Budgeting-Part-One 1.png")
resize_image = image.resize((1200, 250))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image = img)
label1.image = img

# Create a label informing the user about what the program does.
info_lbl_one = Label(home_window, text = "Enjoy a budget plan tailored " +
                 "\nto your financial wants and needs.\n\nBenefit from " +
                 "helpful tips to\nmanage your money.", 
                 font = ("Helvetica", 14))
info_lbl_two = Label(home_window, text = "Aims to improve financial " +
                     "stability among New Zealand tertiary students " +
                     "aged 18-25.", font = ("Helvetica", 10))
 
# Place the labels in a position.
canvas.place(x = 0, y = 20)
exit.place(x = 1110, y = 40)
label1.place(x = 0, y = 450)
info_lbl_one.place(x = 800, y = 280)
info_lbl_two.place(x = 200, y = 400)

home_window.mainloop()