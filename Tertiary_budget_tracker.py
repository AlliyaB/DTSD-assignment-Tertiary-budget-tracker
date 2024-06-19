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

# Funtion to open signup window when button is clicked.
def open_signup_Window():
    # Create window properties.
    signup_window = Toplevel(first_window)
    signup_window.title("Sign up")
    signup_window.geometry("300x350")
    signup_window.resizable(False, False)
    
    # Create window content.
    canvas = Canvas(signup_window, height = 50, width = 350, bg = "CadetBlue2", )
    canvas.place(x = 0, y = 20)
    subtitle_lbl = Label(signup_window, 
                            text = "Create an account",
                            font = ("Helvetica", 15))
    login_btn = tk.Button(signup_window,
                    text = "Log in",
                    width = 10,
                    height = 2,
                    fg = "black",
                    bg = "darkgrey",
                    command = open_login_Window
            )
    # Positioning the labels.
    login_btn.place(x = 200, y = 27)
    #next_btn.place(x = 200, y = 300)
    subtitle_lbl.place(x = 70, y = 80)

    # Declaring name and password as string variables.
    first_name_var=tk.StringVar()
    last_name_var = tk.StringVar()
    username_var = tk.StringVar()
    password_var = tk.StringVar()
    confirm_password_var = tk.StringVar()

    # # Function to validate user input.
    # # Function to validate inputs.
    # def validate_inputs():
    #     first_name = first_name_var.get()
    #     last_name = last_name_var.get()
    #     username = username_var.get()
    #     password = password_var.get()
    #     confirm_password = confirm_password_var.get()

    #     if not first_name.isalpha():
    #         messagebox.showerror("Invalid Input", "First name must contain only letters.")
    #         return False
    #     if not last_name.isalpha():
    #         messagebox.showerror("Invalid Input", "Last name must contain only letters.")
    #         return False
    #     if not first_name or not last_name or not username or not password or not confirm_password:
    #         messagebox.showerror("Missing Fields", "All fields are required.")
    #         return False
    #     if password != confirm_password:
    #         messagebox.showerror("Password Error", "Passwords do not match.")
    #         return False
    #     messagebox.place()
    #     return True

    # Function to get the name and password and print them on the screen.
    def signup():

        first_name = first_name_var.get()
        last_name = last_name_var.get()
        username = username_var.get()
        password=password_var.get()
        confirm_password = confirm_password_var.get()
        
        print("First name: " + first_name)
        print("Last name: " + last_name)
        print("Username: " + username)
        print("Password: " + password)
        print("Confirm password: " + confirm_password)
        
        # Storing user input in a file.
        storing_name = open("Existing Users.txt", "a")
        storing_name.write(f"Full name: {first_name} {last_name} Username: {username} Password: {password}")
        storing_name.write("\n")
        storing_name.close()

        first_name_var.set("")
        last_name_var.set("")
        username_var.set("")
        password_var.set("")
        confirm_password_var.set("")
        
    # Labels.
    first_name_lbl = tk.Label(signup_window, text = "First name:", font=("Helvetica", 10, "bold"))
    last_name_lbl = tk.Label(signup_window, text = "Last name:", font=("Helvetica", 10, "bold"))
    username_lbl = tk.Label(signup_window, text = "Username:", font=("Helvetica", 10, "bold"))
    password_lbl = tk.Label(signup_window, text = "Password:", font = ("Helvetica", 10, "bold"))
    confirm_password_lbl = tk.Label(signup_window, text = "Confirm \nPassword:", font = ("Helvetica", 10, "bold"))
    signup_btn = tk.Button(signup_window,
                    text = "Sign up", 
                    width = 7,
                    height = 1,
                    fg = "black",
                    bg = "gold",
                    command = signup)

    # Entrys and validation.
    first_name_entry = tk.Entry(signup_window, textvariable = first_name_var, font=("Helvetica", 10))
    last_name_entry = tk.Entry(signup_window, textvariable = last_name_var, font=("Helvetica", 10))
    username_entry = tk.Entry(signup_window, textvariable = username_var, font=("Helvetica", 10))
    password_entry=tk.Entry(signup_window, textvariable = password_var, font = ("Helvetica", 10), show = "*")
    confirm_password_entry=tk.Entry(signup_window, textvariable = confirm_password_var, font = ("Helvetica", 10), show = "*")

    # Placing the labels and entries.
    first_name_lbl.place(x=20, y=120)
    first_name_entry.place(x=100, y=120)

    last_name_lbl.place(x=20, y=160)
    last_name_entry.place(x=100, y=160)

    username_lbl.place(x=20, y=200)
    username_entry.place(x=100, y=200)

    password_lbl.place(x=20, y=240)
    password_entry.place(x=100, y=240)

    confirm_password_lbl.place(x=20, y=280)
    confirm_password_entry.place(x=100, y=280)

    signup_btn.place(x=120, y=315)

# Function to open log in window when button is clicked.
def open_login_Window():
    # Create window properties.
    login_window = Toplevel(first_window)
    login_window.title("Log in")
    login_window.geometry("300x350")
    login_window.resizable(False, False)

    # Create window content.
    canvas = Canvas(login_window, height = 50, width = 350, bg = "CadetBlue2", )
    canvas.place(x = 0, y = 20)
    subtitle_lbl = Label(login_window, 
                            text = "Log in to your account",
                            font = ("Helvetica", 15))
    open_signup_btn = tk.Button(login_window,
                    text = "Sign up",
                    width = 10,
                    height = 2,
                    fg = "black",
                    bg = "darkgrey",
                    command = open_signup_Window
            )
    # Create labels for username and password.
    username_lbl = tk.Label(login_window, text = "Username:", font=("Helvetica", 10, "bold"))
    password_lbl = tk.Label(login_window, text = "Password:", font = ("Helvetica", 10, "bold"))

    # Create entries
    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show="*")

    # Place the labels and entries.
    open_signup_btn.place(x = 200, y = 27)
    subtitle_lbl.place(x = 60, y = 80)
    username_lbl.place(x=20, y=160)
    username_entry.place(x=100, y=160)
    password_lbl.place(x=20, y=200)
    password_entry.place(x=100, y=200)

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
open_signup_btn = tk.Button(first_window,
                   text = "Sign up",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "darkgrey",
                   command = open_signup_Window
)

login_btn = tk.Button(first_window,
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
login_btn.place(x = 900, y = 40)
open_signup_btn.place(x = 990, y = 40)
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