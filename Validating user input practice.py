import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # You can add your own validation logic here
    if username == "admin" and password == "password":
        messagebox.showinfo(f"Login Successful", "Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
login_window = tk.Tk()
login_window.title("Login")

# Create and place the username label and entry
username_label = tk.Label(login_window, text="username:")
username_label.pack()

username_entry = tk.Entry(login_window)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(login_window, text="Password:")
password_label.pack()

password_entry = tk.Entry(login_window, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(login_window, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
login_window.mainloop()