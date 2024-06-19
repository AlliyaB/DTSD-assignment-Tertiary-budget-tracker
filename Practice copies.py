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
    signup_window.geometry("300x350")
    # Create the frame and buttons at the top of the page.
    canvas = Canvas(signup_window, height = 50, width = 350, bg = "CadetBlue2", )
    canvas.place(x = 0, y = 20)
    login = tk.Button(signup_window,
                   text = "Log in",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "darkgrey",
                   command = open_login_Window
    )
    login.place(x = 200, y = 27)
    # Create the labels inside this window.
    subtitle_lbl = Label(signup_window, 
                         text = "Create an account",
                         font = ("Helvetica", 15))
    firstname_lbl = Label(signup_window, text = "First Name: ")
    lastname_lbl = Label(signup_window, text = "Last Name: ")
    password_lbl = Label(signup_window, text = "Create Password: ")
    confirmpassword_lbl = Label(signup_window, text = "Confirm password: ")
    # Set the position of the labels.
    subtitle_lbl.place(x = 70, y = 100)
    firstname_lbl.place(x = 0, y = 100)
    lastname_lbl.place(x = 70, y = 100)
    password_lbl.place(x = 70, y = 100)
    confirmpassword_lbl.place(x = 70, y = 100)

def open_login_Window():
    login_window = Toplevel(first_window)
    login_window.title("Log in")
    login_window.geometry("300x350")

# Create Log in/sign up window.
first_window = tk.Tk()
first_window.geometry("1200x750")
first_window.title("Log in/Sign up")
first_window.resizable(False, False)

# Display label.
program_title = tk.Label(first_window,
    text = "Tertiary Budget \nTracker             ",
    font = ("Helvetica", 48))
program_title.place(x = 200, y = 250)

# Create a coloured box for the top where navigation bar will be.
canvas = Canvas(first_window, height = 100, width = 1210, bg = "CadetBlue2", )
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

image = Image.open("Lean-Budgeting-Part-One 1.png")
 
# Resize the image using resize() method
resize_image = image.resize((1200, 250))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.place(x = 0, y = 450)

first_window.mainloop()

first_window.destroy()