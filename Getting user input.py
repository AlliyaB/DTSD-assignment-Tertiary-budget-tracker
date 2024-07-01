# Import tkinter.
import tkinter as tk
from tkinter import  *
from tkinter.ttk import *
from tkinter import messagebox

# Create window.
signup_window = Tk()
signup_window.geometry("300x350")
signup_window.resizable(False, False)

# Add buttons and display canvas.
canvas = Canvas(signup_window, height = 50, width = 350, bg = "CadetBlue2", )
canvas.place(x = 0, y = 20)
subtitle_lbl = Label(signup_window, 
                         text = "Create an account",
                         font = ("Helvetica", 15))
login = tk.Button(signup_window,
                   text = "Log in",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "darkgrey",
                   command = signup_window
        )
# Positioning the labels.
login.place(x = 200, y = 27)
#next_btn.place(x = 200, y = 300)
subtitle_lbl.place(x = 70, y = 80)

# Declaring name and password as string variables.
first_name_var=tk.StringVar()
last_name_var = tk.StringVar()
username_var = tk.StringVar()
password_var = tk.StringVar()
confirm_password_var = tk.StringVar()

#Function to get the name and password and print them on the screen.

def signup():

    first_name = first_name_var.get()
    last_name = last_name_var.get()
    username = username_var.get()
    password=password_var.get()
    confirm_password = confirm_password_var.get()

    # Validate user input.
    if not first_name.isalpha():
        messagebox.showerror("Invalid Input", "First name must contain only letters.")
    if not last_name.isalpha():
        messagebox.showerror("Invalid Input", "Last name must contain only letters.")
    if not first_name or not last_name or not username or not password or not confirm_password:
        messagebox.showerror("Missing Fields", "All fields are required.")
    if password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match.")
    elif first_name.isalpha() and last_name.isalpha() and password == confirm_password:
        # Storing user input in a file.
        storing_name = open("Existing Users.txt", "a")
        storing_name.write(f"Full name: {first_name} {last_name} Username: {username} Password: {password}")
        storing_name.write("\n")
        storing_name.close()
        print("First name: " + first_name)
        print("Last name: " + last_name)
        print("Username: " + username)
        print("Password: " + password)
        print("Confirm password: " + confirm_password)
        first_name_var.set("")
        last_name_var.set("")
        username_var.set("")
        password_var.set("")
        confirm_password_var.set("")
        messagebox.showinfo("Successful", "Signed in successfully")

# Labels.
first_name_lbl = tk.Label(signup_window, text = "First name:", font=("Helvetica", 10, "bold"))
last_name_lbl = tk.Label(signup_window, text = "Last name:", font=("Helvetica", 10, "bold"))
username_lbl = tk.Label(signup_window, text = "Username:", font=("Helvetica", 10, "bold"))
password_lbl = tk.Label(signup_window, text = "Password:", font = ("Helvetica", 10, "bold"))
confirm_password_lbl = tk.Label(signup_window, text = "Confirm \nPassword:", font = ("Helvetica", 10, "bold"))
sub_btn=tk.Button(signup_window,
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

sub_btn.place(x=120, y=315)

signup_window.mainloop()