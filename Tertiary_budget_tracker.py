# Import tkinter.
import tkinter as tk
from tkinter import  *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image 

# Create a function to double check the user wants to exit before exiting.
def popup():
  response = messagebox.askquestion("Exit Programme?","Your progress will " +
                                  "NOT be saved.\nAre you sure you want " +
                                  "to exit the program?", 
  icon='warning')
  print(response)
  if response == "yes":
    confirm_btn = Button(first_window, command = first_window.quit)
    confirm_btn.pack()
    first_window.destroy()

# Create functions for each of the windows for when a button is clicked.
def open_signup_Window():
    signup_window = Toplevel(first_window)
    signup_window.title("Sign up")
    signup_window.geometry("1200x750")

def open_login_Window():
    login_window = Toplevel(first_window)
    login_window.title("Log in")
    login_window.geometry("1200x750")

# Create Log in/sign up window.
first_window = tk.Tk()
first_window.geometry("1200x750")
first_window.title("Log in/Sign up")
first_window.resizable(False, False)

# Display label.
program_title = tk.Label(first_window,
    text = "Tertiary Budget \nTracker             ",
    font = ("Helvetica", 48),
)
program_title.place(x = 200, y = 250)

# Create a coloured box for the top where navigation bar will be.
canvas = Canvas(first_window, height = 100, width = 1210, bg = "BLUE", )
canvas.place(x = 0, y = 20)

# Create Sign up and log in buttons.
signup = tk.Button(first_window,
                   text = "Sign up",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "darkgrey",
                   command = open_signup_Window
)

login = tk.Button(first_window,
                   text = "Log in",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "darkgrey",
                   command = open_login_Window
)

# Create exit button.
exit = tk.Button(first_window,
                   text = "Exit",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "grey",
                   command = popup
)

# Place the buttons in a position.
login.place(x = 900, y = 40)
signup.place(x = 990, y = 40)
exit.place(x = 1110, y = 40)

# Create a label informing the user about what the program does.
info_lbl_one = Label(first_window, text = "Enjoy a budget plan tailored " +
                 "\nto your financial wants and needs.\n\nBenefit from " +
                 "helpful tips to\nmanage your money.", 
                 font = ("Helvetica", 14))
info_lbl_two = Label(first_window, text = "Aims to improve financial stability among New Zealand tertiary students aged 18-25.", font = ("Helvetica", 10))
info_lbl_one.place(x = 800, y = 280)
info_lbl_two.place(x = 200, y = 400)

# Add image to the first window.
img = ImageTk.PhotoImage(Image.open("Lean-Budgeting-Part-One 1.png")) 
panel = tk.Label(first_window, width = 1210,  
                 height = 250, image = img) 
# Place the image in position.
panel.place(x = 0, y = 450)

first_window.mainloop()

first_window.destroy()