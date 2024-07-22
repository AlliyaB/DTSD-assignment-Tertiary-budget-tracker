# Import tkinter, date, and datetime.
import tkinter as tk
from tkinter import  *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image 
from datetime import datetime
from datetime import date

# Function to ensure the user wants to exit the first_window.
def popup():
  response = messagebox.askquestion("Exit Programme?","Your progress will " +
                                  "NOT be saved.\nAre you sure you want " +
                                  "to exit the program?", 
  icon='warning')
  print(response)
  if response == "yes":
    confirm_btn = Button(first_window, 
                         command = first_window.quit)
    confirm_btn.pack()
    first_window.destroy()

# Funtion to open signup window when button is clicked.
def open_signup_Window():
    # Function to validate user input and submit it to a file.
    # Direct user to building profile page after signing in.
    def signup():
        # Function to ensure the user wants to exit the building_profile_window.
        def popup():
            response = messagebox.askquestion("Exit Programme?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to exit the program?", 
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(building_profile_window, 
                                     command = building_profile_window.quit)
                confirm_btn.pack()
                building_profile_window.destroy()
        
        def calculate_age(birth_date: datetime) -> int:
            """Function to carry out age calculation based off birthdate 
            (dd/mm/yyyy).
            """
            # Get today's date.
            today: date = date.today()
            # Calculate the year difference between today and the date of birth.
            difference: int = today.year - birth_date.year
            # Find out if today preceeds the date of birth this year.
            today_preceeds_DOB: int = int((today.month, today.day) <
                                        (birth_date.month, birth_date.day))
            age: int = difference - today_preceeds_DOB
            return age
        
        # Function to output message when tertiary button is clicked.
        def output_message():
            tertiary_status = tertiary_status_var.get()
            knowledge = knowledge_var.get()
            if tertiary_status == "1":
                messagebox.showinfo("Target market", "This program is specifically designed for tertiary students like you.")
            elif tertiary_status == "2":
                messagebox.showinfo("Not target market", "This program is specifically designed for tertiary students.\nHowever you're welcome to it's benefits.")
            else:
                messagebox.showerror("Invalid input", "There are missing fields.\nPlease select a tertiary status.")

        first_name = first_name_var.get()
        last_name = last_name_var.get()
        username = username_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        # Validate the user input if all fields are entered.
        if first_name and last_name and username and password and confirm_password:
            try:
                with open("Existing Users.txt", "r") as file:
                    usernames = file.read().splitlines()
            except FileNotFoundError:
                usernames = []
            if not username.isalpha() and not username.isnumeric():
                messagebox.showerror("Invalid username", "Please only " +
                                     "enter numbers or letters for username.")
            elif username in usernames:
                messagebox.showerror("Invalid username", "This username " +
                                     "already exists.\nPlease enter a " +
                                     "different username.")
            elif not first_name.isalpha() or not last_name.isalpha():
                messagebox.showerror("Invalid first name/last " +
                                     "name", "Please only enter letters " +
                                     "for first name and last name.")
            elif password != confirm_password:
                messagebox.showerror("Invalid password", "Please check " +
                                     "that your passwords match.")
            else:
                with open("Existing Users.txt", "a") as file:
                    file.write(f"{username}\n")
                    file.write(f"Full name: {first_name} {last_name} " +
                               f"Username: {username} Password: {password}\n")
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
                messagebox.showinfo("Successful", "Sign up successful." +
                                    f"\nWelcome {username}")
                first_window.destroy()

                # Create building profile page, user will be directed here 
                # after signing up.

                building_profile_window = tk.Tk()
                building_profile_window.geometry("300x350")
                building_profile_window.title("Building profile")
                building_profile_window.resizable(False, False)

                # Print today's date, neccassary for calculating the users age.
                # Print todays date.
                today = date.today()
                d = today.strftime("%d/%m/%y")
                print(f"Date: {d}")

                # Declaring birthdate, tertiary status, and knowledge as string variables.
                birthdate_var = tk.StringVar()
                tertiary_status_var = StringVar(building_profile_window, "1") 
                knowledge_var = tk.StringVar()

                # Create window content with labels, canvas, and buttons.
                canvas = Canvas(building_profile_window, 
                                height = 50, 
                                width = 350, 
                                bg = "CadetBlue2", )
                title_lbl = tk.Label(building_profile_window, 
                                     text = "Building profile:", 
                                     font = ("Helvetica", 15),
                                     bg = "CadetBlue2")
                subtitle_lbl = tk.Label(building_profile_window, 
                                       text = f"Let's get to know you better!\nPlease enter the following",
                                       font = ("Helvetica", 10))
                exit = tk.Button(building_profile_window,
                                 text = "Exit",
                                 width = 10,
                                 height = 2,
                                 fg = "black",
                                 bg = "grey",
                                 command = popup)    
                
                next_btn = tk.Button(building_profile_window,
                           text = "Next", 
                           width = 7,
                           height = 1,
                           fg = "black",
                           bg = "gold")
                
                birthdate_lbl = tk.Label(building_profile_window, 
                              text = "Birthdate (dd/mm/yyyy):", 
                              font = ("Helvetica", 10, "bold"))
                tertiary_lbl = tk.Label(building_profile_window, 
                                        text = "Tertiary status:", 
                                        font = ("Helvetica", 10, "bold"))
                knowledge_lbl = tk.Label(building_profile_window, 
                                        text = "Knowledge of budgeting:", 
                                        font = ("Helvetica", 10, "bold"))

                # Entrys.
                birthdate_entry = tk.Entry(building_profile_window, 
                                            textvariable = birthdate_var)

                # Dictionary to create multiple options for tertiary status.
                tertiary_status_dict = {"Current student" : "1", 
                                        "Other" : "2"} 
                # Use a loop to create multiple radiobuttons for tertiary status.
                x_coord = 20
                for (text, value) in tertiary_status_dict.items(): 
                    tertiary_status_btn = Radiobutton(building_profile_window, 
                                                      text = text, 
                                                      variable = tertiary_status_var,
                                                      value = value,
                                                      command = output_message)
                    tertiary_status_btn.place(x = x_coord, y = 212.5)
                    x_coord += 112 # Provide distance between buttons.

                # Dictionary to create multiple options for knowledge entry.
                knowledge_dict = {"Very Poor" : "1",
                                  "Average" : "3",
                                  "Excellent" : "5"}
                
                # Use a loop to create multiple radiobuttons for knowledge.
                x_coord = 20
                for (text, value) in knowledge_dict.items(): 
                    knowledge_btn = Radiobutton(building_profile_window, 
                                                text = text, 
                                                variable = knowledge_var,
                                                value = value)
                    knowledge_btn.place(x = x_coord, y = 270)
                    x_coord += 87
                
                # Placing the labels and entries.
                canvas.place(x = 0, y = 20)
                title_lbl.place(x = 10, y = 34)
                subtitle_lbl.place(x = 60, y = 80)
                exit.place(x = 200, y = 27)
                next_btn.place(x = 120, y = 315)

                birthdate_lbl.place(x = 20, y = 130)
                birthdate_entry.place(x = 20, y = 155)

                tertiary_lbl.place(x = 20, y = 187.5)

                knowledge_lbl.place(x = 20, y = 245)

                building_profile_window.mainloop()

        else:
            messagebox.showerror("Invalid input", "There are missing " +
                                 "fields.\nPlease enter all fields.")

    # Create window properties.
    signup_window = Toplevel(first_window)
    signup_window.title("Sign up")
    signup_window.geometry("300x350")
    signup_window.resizable(False, False)

    # Declaring name and password as string variables.
    first_name_var = tk.StringVar()
    last_name_var = tk.StringVar()
    username_var = tk.StringVar()
    password_var = tk.StringVar()
    confirm_password_var = tk.StringVar()
    
    # Create window content with labels, canvas, and buttons.
    canvas = Canvas(signup_window, 
                    height = 50, 
                    width = 350, 
                    bg = "CadetBlue2")
    title_lbl = tk.Label(signup_window, 
                      text = "Sign up:", 
                      font = ("Helvetica", 15),
                      bg = "CadetBlue2")
    subtitle_lbl = tk.Label(signup_window, 
                        text = "Create an account",
                        font = ("Helvetica", 15))
    login_btn = tk.Button(signup_window,
                          text = "Log in",
                          width = 10,
                          height = 2,
                          fg = "black",
                          bg = "darkgrey",
                          command = open_login_Window)
            
    first_name_lbl = tk.Label(signup_window, 
                              text = "First name:", 
                              font = ("Helvetica", 10, "bold"))
    last_name_lbl = tk.Label(signup_window, 
                             text = "Last name:", 
                             font = ("Helvetica", 10, "bold"))
    username_lbl = tk.Label(signup_window, 
                            text = "Username:", 
                            font = ("Helvetica", 10, "bold"))
    password_lbl = tk.Label(signup_window, 
                            text = "Password:", 
                            font = ("Helvetica", 10, "bold"))
    confirm_password_lbl = tk.Label(signup_window, 
                                    text = "Confirm \nPassword:", 
                                    font = ("Helvetica", 10, "bold"))
    signup_btn = tk.Button(signup_window,
                           text = "Sign up", 
                           width = 7,
                           height = 1,
                           fg = "black",
                           bg = "gold",
                           command = signup)

    # Entrys.
    first_name_entry = tk.Entry(signup_window, 
                                textvariable = first_name_var)
    last_name_entry = tk.Entry(signup_window, 
                               textvariable = last_name_var)
    username_entry = tk.Entry(signup_window, 
                              textvariable = username_var)
    password_entry=tk.Entry(signup_window, 
                            textvariable = password_var, 
                            show = "*")
    confirm_password_entry=tk.Entry(signup_window, 
                                    textvariable = confirm_password_var, 
                                    show = "*")

    # Placing the labels and entries.
    canvas.place(x = 0, y = 20)
    login_btn.place(x = 200, y = 27)
    title_lbl.place(x = 10, y = 36)
    subtitle_lbl.place(x = 70, y = 80)

    first_name_lbl.place(x = 20, y = 120)
    first_name_entry.place(x = 100, y = 120)

    last_name_lbl.place(x = 20, y = 160)
    last_name_entry.place(x = 100, y = 160)

    username_lbl.place(x = 20, y = 200)
    username_entry.place(x = 100, y = 200)

    password_lbl.place(x = 20, y = 240)
    password_entry.place(x = 100, y = 240)

    confirm_password_lbl.place(x = 20, y = 280)
    confirm_password_entry.place(x = 100, y = 280)

    signup_btn.place(x = 120, y = 315)

# Function to open log in window when button is clicked.
def open_login_Window():
    # Function to validate user input and check the user exists in file.
    def login():

        username = username_var.get()
        password = password_var.get()

        if username and password:
            try:
                with open("Existing Users.txt", "r") as file:
                    lines = file.read().splitlines()
                    # Check if a line has username and password.
                    user_exists = any(f"Username: {username}" in line and f"Password: {password}" in line for line in lines)
                if user_exists:
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    username_var.set("")
                    password_var.set("")
                    messagebox.showinfo("Successful", f"Log in successful." +
                                        f"\nWelcome back {username}")
                elif not user_exists:
                    messagebox.showerror("Unsuccessful", "You have entered " +
                                     "an invalid username or password. " +
                                     "Please try again or sign up.")
            except FileNotFoundError:
                messagebox.showerror("Unsuccessful", "You have entered " +
                                     "an invalid username or password. " +
                                     "Please try again or sign up.")
        else:
            messagebox.showerror("Invalid input", "There are missing " +
                                 "fields.\nPlease enter all fields.")

    # Create window properties.
    login_window = Toplevel(first_window)
    login_window.title("Log in")
    login_window.geometry("300x350")
    login_window.resizable(False, False)

    # # Calculate center position. Keep windows centred each time it's opened.
    # window_width = 300
    # window_height = 350
    # screen_width = login_window.winfo_screenwidth()
    # screen_height = login_window.winfo_screenheight()

    # x_position = (screen_width - window_width) // 2
    # y_position = (screen_height - window_height) // 4

    # # Set window geometry
    # login_window.geometry(f"{window_width} x {window_height} + {x_position} + {y_position}")

    # Declaring username and password as string variables.
    username_var = tk.StringVar()
    password_var = tk.StringVar()

    # Create window content with labels, canvas, and buttons.
    canvas = Canvas(login_window, 
                    height = 50, 
                    width = 350, 
                    bg = "CadetBlue2")
    title_lbl = tk.Label(login_window, 
                         text = "Log in:", 
                         font = ("Helvetica", 15),
                         bg = "CadetBlue2")
    subtitle_lbl = tk.Label(login_window,
                         text = "Log in to your account",
                         font = ("Helvetica", 15))
    open_signup_btn = tk.Button(login_window,
                                text = "Sign up",
                                width = 10,
                                height = 2,
                                fg = "black",
                                bg = "darkgrey",
                                command = open_signup_Window)

    username_lbl = tk.Label(login_window, 
                            text = "Username:", 
                            font=("Helvetica", 10, "bold"))
    password_lbl = tk.Label(login_window, 
                            text = "Password:", 
                            font = ("Helvetica", 10, "bold"))
    login_btn = tk.Button(login_window,
                          text = "Log in", 
                          width = 7,
                          height = 1,
                          fg = "black",
                          bg = "gold",
                          command = login)

    # Create entries
    username_entry = tk.Entry(login_window, 
                              textvariable = username_var)
    password_entry = tk.Entry(login_window, 
                              textvariable = password_var, 
                              show = "*")

    # Place the labels and entries.
    canvas.place(x = 0, y = 20)
    open_signup_btn.place(x = 200, y = 27)
    title_lbl.place(x = 10, y = 36)
    subtitle_lbl.place(x = 60, y = 80)
    username_lbl.place(x = 20, y = 160)
    username_entry.place(x = 100, y = 160)
    password_lbl.place(x = 20, y = 200)
    password_entry.place(x = 100, y = 200)
    login_btn.place(x = 120, y = 315)

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
                   command = open_signup_Window)
login_btn = tk.Button(first_window,
                   text = "Log in",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "darkgrey",
                   command = open_login_Window)

# Create exit button.
exit = tk.Button(first_window,
                   text = "Exit",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "grey",
                   command = popup)

# Place the buttons in a position.
login_btn.place(x = 900, y = 40)
open_signup_btn.place(x = 990, y = 40)
exit.place(x = 1110, y = 40)

# Create a label informing the user about what the program does.
info_lbl_one = Label(first_window, text = "Enjoy a budget plan tailored " +
                 "\nto your financial wants and needs.\n\nBenefit from " +
                 "helpful tips to\nmanage your money.", 
                 font = ("Helvetica", 14))
info_lbl_two = Label(first_window, text = "Aims to improve financial " +
                     "stability among New Zealand tertiary students " +
                     "aged 18-25.", font = ("Helvetica", 10))
info_lbl_one.place(x = 800, y = 280)
info_lbl_two.place(x = 200, y = 400)

# Add image to the first window.
image = Image.open("Lean-Budgeting-Part-One 1.png")
 
# Resize the image using resize() method
resize_image = image.resize((1200, 250))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image = img)
label1.image = img
label1.place(x = 0, y = 450)

first_window.mainloop()