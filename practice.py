# Import tkinter, date, and datetime.
import tkinter as tk
from tkinter import  *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image 
from datetime import datetime
from datetime import date
from tkinter import font
import sys;
from tkinter import ttk 

def open_first_window():
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
    # Create Log in/sign up window.
    global first_window
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
    canvas = Canvas(first_window, 
                    height = 100, 
                    width = 1210, 
                    bg = "CadetBlue2")

    # Create Sign up, log in, and exit buttons.
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
    exit = tk.Button(first_window,
                    text = "Exit",
                    width = 10,
                    height = 2,
                    fg = "black",
                    bg = "grey",
                    command = popup)

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

    # Place labels, buttons, and images in a position.
    canvas.place(x = 0, y = 20)
    login_btn.place(x = 900, y = 40)
    open_signup_btn.place(x = 990, y = 40)
    exit.place(x = 1110, y = 40)
    label1.place(x = 0, y = 450)

    first_window.mainloop()

# Funtion to open signup window when button is clicked.
def open_signup_Window():

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

        # Function to output message when tertiary button is clicked.
        def tertiary_message():
            tertiary_status = tertiary_status_var.get()
            if tertiary_status == "1":
                messagebox.showinfo("Note", "Please enjoy this applications " +
                                    "features and resources which are " +
                                    "tailored specifically for tertiary " +
                                    "students like yourself.")
            elif tertiary_status == "2":
                messagebox.showinfo("Note", "Please note that this " +
                                    "application is primarily designed for " +
                                    "tertiary students, and may not meet " +
                                    "your individual needs.")
            else:
                messagebox.showerror("Invalid input", "There are missing fields.\nPlease select a tertiary status.")

        # Function to output message when knowledge button is clicked.
        def knowledge_message():
            knowledge = knowledge_var.get()
            if knowledge == "1":
                messagebox.showinfo("Introduction", "A budget is a " +
                                    "generated spending plan based off your " +
                                    "financial wants and needs. It includes " +
                                    "prioritizing and allocating various " +
                                    "incomes, ensuring that all expenses " +
                                    "are covered without spending more " +
                                    "than what is earned. Through this " +
                                    "application, budgeting can provide " +
                                    "clarity, preparedness and insights " +
                                    "around finances, savings goals, and " +
                                    "expensive emergencies. Ultimately, " +
                                    "budgeting improves financial stability.")
            elif knowledge == "2":
                messagebox.showinfo("Aknowledgement", "Great start to " +
                                    "improving your financial " +
                                    "stability. \nKeep progressing!")
            elif knowledge == "3":
                messagebox.showinfo("Aknowledgement", "Great progression in " +
                                    "your journey to financial stability." +
                                    "\nKeep up the great work!")
            else:
                messagebox.showerror("Invalid input", "There are missing fields.\nPlease select a tertiary status.")

        # Function to validate the user input on building profile page and redirect to homepage.
        def next():
            birthdate = birthdate_var.get()
            knowledge = knowledge_var.get()
            tertiary_status = tertiary_status_var.get()
            try:
                # Convert the string to a datetime object
                birthdate = datetime.strptime(birthdate, '%d/%m/%Y')
                # Get todays date.
                today = date.today()
                # Find the difference between today and the date of birth.
                difference = today.year - birthdate.year
                # Find out if today preceeds the date of birth this year.
                today_precedes_DOB = (today.month, today.day) < (birthdate.month, birthdate.day)
                age = difference - today_precedes_DOB
            except ValueError:
                # Show an error if the date format is incorrect
                messagebox.showerror("Invalid input", "Please enter a valid birthdate (dd/mm/yyyy)")
            if age <= 0 or age > 99:
                messagebox.showerror("Invalid input", "Please enter a valid birthdate(dd/mm/yyyy)")
                return False
            elif age < 18 or age > 25:
                age_maybe = messagebox.askquestion("Note", "Please note that this " +
                                    "application is primarily designed for " +
                                    "ages 18-25, and may not meet " +
                                    "your individual needs.\n\nAre you sure you want to continue?")
                if age_maybe == "no":
                    return False
            elif knowledge == "":
                messagebox.showerror("Invalid input", "Please select your level of knowledge.")
                return False
            elif tertiary_status == "":
                messagebox.showerror("Invalid input", "Please select your current tertiary status.")
                return False
            else:
                messagebox.showinfo("Note", "Please enjoy this applications " +
                                    "features and resources which are " +
                                    "tailored specifically for ages 18-25 " +
                                    "like yourself.")
                if tertiary_status == "1":
                    tertiary_status_words = "Current student"
                if tertiary_status == "2":
                    tertiary_status_words = "Other"
                if knowledge == "1":
                    knowledge_words = "Very poor"
                if knowledge == "2":
                    knowledge_words = "Average"
                if knowledge == "3":
                    knowledge_words = "Excellent"
                with open("Existing Users.txt", "a") as file:
                    file.write(f"Birthdate: {birthdate} Tertiary status: {tertiary_status_words} Knowledge of budgeting: {knowledge_words}\n\n")
                print(f"Birthdate: {birthdate}")
                print(f"Tertiary status: {tertiary_status_words}")
                print(f"Knowledge of budgeting: {knowledge_words}")
                exit_signup_window()

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
                global building_profile_window
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
                tertiary_status_var = StringVar() 
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
                           bg = "gold",
                           command = next)
                
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
                                                      command = tertiary_message)
                    tertiary_status_btn.place(x = x_coord, y = 212.5)
                    x_coord += 112 # Provide distance between buttons.

                # Dictionary to create multiple options for knowledge entry.
                knowledge_dict = {"Very Poor" : "1",
                                  "Average" : "2",
                                  "Excellent" : "3"}
                
                # Use a loop to create multiple radiobuttons for knowledge.
                x_coord = 20
                for (text, value) in knowledge_dict.items(): 
                    knowledge_btn = Radiobutton(building_profile_window, 
                                                text = text,
                                                variable = knowledge_var,
                                                value = value,
                                                command = knowledge_message)
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
    global signup_window
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
    open_login_btn = tk.Button(signup_window,
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
    open_login_btn.place(x = 200, y = 27)
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
    signup_window.mainloop()

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
                    exit_login_window()
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
    global login_window
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

# Function to sign the user out and redirect them to the first window.
def signout():
    response = messagebox.askquestion("Signout?","Your progress will " +
                                        "NOT be saved.\nAre you sure you want " +
                                        "to signout?", 
    icon = 'warning')
    print(response)
    if response == "yes":
        confirm_btn = Button(profile_window)
        confirm_btn.pack()
        if 'home_window' in globals():
            home_window.destroy()
        if 'profile_window' in globals():
            profile_window.destroy()
        open_first_window()

# Function to exit the log in window and go to the main code.
def exit_login_window():
    if 'first_window' in globals():
        first_window.destroy()
    open_main_code()

# Function to exit the sign up window and go to the main code.
def exit_signup_window():
    if 'building_profile_window' in globals():
        building_profile_window.destroy()
    open_main_code()

# Function where the main code is.
def open_main_code():
    # Function to open help window.
    def open_help_window():

        # Function to ensure the user wants to exit the help_window.
        def exit_help_window():
            response = messagebox.askquestion("Exit Programme?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to exit the program?", 
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(help_window, 
                                    command = help_window.quit)
                confirm_btn.pack()
                help_window.destroy()

        # Create profile page. 
        global help_window
        help_window = tk.Tk()
        help_window.geometry("1200x750")
        help_window.title("Help: User Manual")
        help_window.resizable(False, False)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        canvas = Canvas(help_window, 
                        height = 100, 
                        width = 1210, 
                        bg = "CadetBlue2")
        home_btn = tk.Button(help_window,
                        text = "Home",
                        width = 10,
                        height = 2,
                        bg = "darkgrey",
                        command = help_to_main)
        open_about_btn = tk.Button(help_window,
                        text = "About",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = help_to_about)
        open_budget_btn = tk.Button(help_window,
                        text = "My Budget",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey")
        open_tips_btn = tk.Button(help_window,
                        text = "Tips",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = tips_message)
        open_help_btn = tk.Button(help_window,
                        text = "Help",
                        font = underlined_font,
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey")
        profile_btn = tk.Button(help_window,
                        text = "Profile",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = open_profile)
        exit = tk.Button(help_window,
                        text = "Exit",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = exit_help_window)
        
        # Create user manual file.
        user_manual_file = open("User_manual.txt","rb")
        user_manual = user_manual_file.read()

        # Create a vertical scrollbar where the user manual is displayed.
        scrollbar = Scrollbar(help_window)
        text_box = Text(help_window,
                        width = 120, 
                        height = 37, 
                        wrap = NONE, 
                        yscrollcommand = scrollbar.set)
        text_box.insert(END, user_manual)
        scrollbar.config(command = text_box.yview)

        # Place labels, buttons, and images in a position.
        canvas.place(x = 0, y = 20)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit.place(x = 1110, y = 40)
        scrollbar.pack(side = RIGHT, fill = Y)
        text_box.pack(side = BOTTOM)

        help_window.mainloop()

    # Function to open my income page.
    def open_my_income():

        # Function to ensure the user wants to exit the help_window.
        def exit_income_window():
            response = messagebox.askquestion("Exit Programme?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to exit the program?", 
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(income_window, 
                                    command = income_window.quit)
                confirm_btn.pack()
                income_window.destroy()

        # Function to create income table.
        def create_table(income_window):
            income_lbl = tk.Label(income_window, 
                            text = "Income type:", 
                            font = ("Helevitica", 15, "bold"))

            income_type_var = tk.StringVar() 
            income_choice = ttk.Combobox(income_window, width = 17, 
                                        textvariable = income_type_var) 

            # Adding combobox drop down list 
            income_choice["values"] = ("Weekly",
                                       "Fortnightly",
                                       "Four-weekly",
                                       "Monthly",
                                       "Yearly") 

            # Shows weekly as a default value 
            income_choice.current(0)

            income_type = income_type_var.get()

            # Create labels for each of the income types and the total income.
            type_1_lbl = tk.Label(income_window,
                                  text = "Ongoing employment $", 
                                  font=("Helvetica", 15, "bold"))
            type_2_lbl = tk.Label(income_window, 
                                  text = "Study link loan/student allowance $", 
                                  font=("Helvetica", 15, "bold"))
            type_3_lbl = tk.Label(income_window, 
                                    text = "Holiday/work savings $", 
                                    font=("Helvetica", 15, "bold"))
            type_4_lbl = tk.Label(income_window, 
                                    text = "Grants/scholarships $", 
                                    font=("Helvetica", 15, "bold"))
            type_5_lbl = tk.Label(income_window, 
                                    text = "Family $", 
                                    font=("Helvetica", 15, "bold"))
            type_6_lbl = tk.Label(income_window, 
                                    text = "One off jobs $", 
                                    font=("Helvetica", 15, "bold"))
            type_7_lbl = tk.Label(income_window, 
                                    text = "Other income $", 
                                    font=("Helvetica", 15, "bold"))
            type_8_lbl = tk.Label(income_window, 
                                    text = f"Total {income_type} income$", 
                                    font=("Helvetica", 15, "bold"))
            
            # Create entries for each income type.
            type_1_entry = tk.Entry(income_window)
            type_2_entry = tk.Entry(income_window)
            type_3_entry = tk.Entry(income_window)
            type_4_entry = tk.Entry(income_window)
            type_5_entry = tk.Entry(income_window)
            type_6_entry = tk.Entry(income_window)
            type_7_entry = tk.Entry(income_window)
            type_8_entry = tk.Entry(income_window)

            # Place the labels.
            income_lbl.place(x = 300, y = 300)
            income_choice.place(x = 660, y = 305)
            type_1_lbl.place(x = 300, y = 350)
            type_1_entry.place(x = 660, y = 355)
            type_2_lbl.place(x = 300, y = 390)
            type_2_entry.place(x = 660, y = 395)
            type_3_lbl.place(x = 300, y = 430)
            type_3_entry.place(x = 660, y = 435)
            type_4_lbl.place(x = 300, y = 470)
            type_4_entry.place(x = 660, y = 475)
            type_5_lbl.place(x = 300, y = 510)
            type_5_entry.place(x = 660, y = 515)
            type_6_lbl.place(x = 300, y = 550)
            type_6_entry.place(x = 660, y = 555)
            type_7_lbl.place(x = 300, y = 590)
            type_7_entry.place(x = 660, y = 595)
            type_8_lbl.place(x = 300, y = 630)
            type_8_entry.place(x = 660, y = 635)

        # Function to save the user income, validate their entries, and redirect to expenses page.
        def income_next():
            income_1 = income_1_entry.get()

        # Create my income page.
        global income_window
        income_window = tk.Tk()
        income_window.geometry("1200x750")
        income_window.title("My income")
        income_window.resizable(False, False)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        title = tk.Label(income_window, 
                         text = "My income:",
                         font = ("Helvetica", 40))
        description_lbl = tk.Label(income_window,
                                   text = "Please enter your amount to " +
                                          "budget (income) below, you can " +
                                          "choose weekly, fortnightly, " +
                                          "four-weekly, monthly or yearly " +
                                          "amounts.\nThis program will " +
                                          "calculate the total income for " +
                                          "you.",
                                   justify = LEFT)
        canvas = Canvas(income_window, 
                        height = 100, 
                        width = 1210, 
                        bg = "CadetBlue2")
        home_btn = tk.Button(income_window,
                        text = "Home",
                        width = 10,
                        height = 2,
                        bg = "darkgrey",
                        command = income_to_main)
        open_about_btn = tk.Button(income_window,
                        text = "About",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = income_to_about)
        open_budget_btn = tk.Button(income_window,
                        text = "My Budget",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey")
        open_tips_btn = tk.Button(income_window,
                        text = "Tips",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = tips_message)
        open_help_btn = tk.Button(income_window,
                        text = "Help",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = income_to_help)
        profile_btn = tk.Button(income_window,
                        text = "Profile",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = open_profile)
        exit = tk.Button(income_window,
                        text = "Exit",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = exit_income_window)
        next_btn = tk.Button(income_window,
                        text = "Next",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "gold") # Command, take user to next stage
        back_btn = tk.Button(income_window,
                        text = "Back",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = income_to_main)
        # Create progress bar on the side.
        side_bar = Canvas(income_window, 
                        height = 900, 
                        width = 140, 
                        bg = "CadetBlue2")
        income_btn = tk.Button(income_window,
                               text = "My Income",
                               font = underlined_font)
        expense_btn = tk.Button(income_window,
                                text = "My expenses",
                                command = open_expenses)
        budget_btn = tk.Button(income_window,
                                text = "My budget")
        insights_btn = tk.Button(income_window,
                                text = "My insights")
        # Income image.
        image = Image.open("income icon.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        income_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        income_image.image = img

        # Expense image.
        image = Image.open("expense_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        expense_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        expense_image.image = img

        # Budget image.
        image = Image.open("budget_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        budget_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        budget_image.image = img

        # Insights image.
        image = Image.open("insights_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        insights_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        insights_image.image = img

        # Add income table.
        create_table(income_window)
        
        # Place labels, buttons, and images in a position.
        title.place(x = 200, y = 150)
        description_lbl.place(x = 200, y = 220)
        canvas.place(x = 0, y = 20)
        side_bar.place(x = 0, y = 122)
        income_btn.place(x = 40, y = 250)
        income_image.place(x = 50, y = 190)
        expense_btn.place(x = 40, y = 360)
        expense_image.place(x = 50, y = 300)
        budget_btn.place(x = 40, y = 470)
        budget_image.place(x = 50, y = 410)
        insights_btn.place(x = 40, y = 580)
        insights_image.place(x = 50, y = 520)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit.place(x = 1110, y = 40)
        next_btn.place(x = 1110, y = 700)
        back_btn.place(x = 150, y = 700)

        income_window.mainloop()

    # Function to open my expenses page.
    def open_expenses():

        # Function to ensure the user wants to exit the help_window.
        def exit_expenses_window():
            response = messagebox.askquestion("Exit Programme?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to exit the program?", 
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(expenses_window, 
                                    command = expenses_window.quit)
                confirm_btn.pack()
                expenses_window.destroy()

        # Create my income page.
        income_window.destroy()
        global expenses_window
        expenses_window = tk.Tk()
        expenses_window.geometry("1200x750")
        expenses_window.title("My expenses")
        expenses_window.resizable(False, False)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        title = tk.Label(expenses_window, 
                         text = "My expenses",
                         font = ("Helvetica", 40))
        canvas = Canvas(expenses_window, 
                        height = 100, 
                        width = 1210, 
                        bg = "CadetBlue2")
        home_btn = tk.Button(expenses_window,
                        text = "Home",
                        width = 10,
                        height = 2,
                        bg = "darkgrey",
                        command = expenses_to_main)
        open_about_btn = tk.Button(expenses_window,
                        text = "About",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = expenses_to_about)
        open_budget_btn = tk.Button(expenses_window,
                        text = "My Budget",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey")
        open_tips_btn = tk.Button(expenses_window,
                        text = "Tips",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = tips_message)
        open_help_btn = tk.Button(expenses_window,
                        text = "Help",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = expenses_to_help)
        profile_btn = tk.Button(expenses_window,
                        text = "Profile",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = open_profile)
        exit = tk.Button(expenses_window,
                        text = "Exit",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = exit_expenses_window)
        next_btn = tk.Button(expenses_window,
                        text = "Next",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "gold") # Command, take user to next stage
        back_btn = tk.Button(expenses_window,
                        text = "Back",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = expenses_to_income)
        # Create progress bar on the side.
        side_bar = Canvas(expenses_window, 
                        height = 900, 
                        width = 140, 
                        bg = "CadetBlue2")
        income_btn = tk.Button(expenses_window,
                               text = "My Income",
                               command = expenses_to_income)
        expense_btn = tk.Button(expenses_window,
                                text = "My expenses",
                                font = underlined_font)
        budget_btn = tk.Button(expenses_window,
                                text = "My budget")
        insights_btn = tk.Button(expenses_window,
                                text = "My insights")
        # Income image.
        image = Image.open("income icon.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        income_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        income_image.image = img

        # Expense image.
        image = Image.open("expense_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        expense_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        expense_image.image = img

        # Budget image.
        image = Image.open("budget_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        budget_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        budget_image.image = img

        # Insights image.
        image = Image.open("insights_image.png")
        resize_image = image.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)
        insights_image = tk.Label(image = img,
                          bg = "CadetBlue2")
        insights_image.image = img

        # Add expenses table.

        
        # Place labels, buttons, and images in a position.
        title.place(x = 200, y = 150)
        canvas.place(x = 0, y = 20)
        side_bar.place(x = 0, y = 122)
        income_btn.place(x = 40, y = 250)
        income_image.place(x = 50, y = 190)
        expense_btn.place(x = 40, y = 360)
        expense_image.place(x = 50, y = 300)
        budget_btn.place(x = 40, y = 470)
        budget_image.place(x = 50, y = 410)
        insights_btn.place(x = 40, y = 580)
        insights_image.place(x = 50, y = 520)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit.place(x = 1110, y = 40)
        next_btn.place(x = 1110, y = 700)
        back_btn.place(x = 150, y = 700)

        expenses_window.mainloop()

    # Function to ensure the user wants to exit the home_window.
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

    # Function to inform the user that the tips page is unavailable.
    def tips_message():
        messagebox.showerror("Error", "Page not found. Sorry, financial " +
                             "tips are currently unavailable. :(")

    # Function to show the user their profile and allow them to edit information.
    def open_profile():
        # Function to exit profile page.
        def exit_profile():
            response = messagebox.askquestion("Exit profile?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to exit the profile?", 
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(profile_window, 
                                    command = profile_window.quit)
                confirm_btn.pack()
                profile_window.destroy()

        # Create profile page.
        global profile_window
        profile_window = tk.Toplevel()
        profile_window.geometry("300x350")
        profile_window.title("Profile")
        profile_window.resizable(False, False)

        # Read the user profile information from the existing users file.
        with open("Existing Users.txt", "r") as file:
            lines = file.read().splitlines()
            print(lines)

        # Create widow content.
        canvas = Canvas(profile_window, 
                        height = 50, 
                        width = 350, 
                        bg = "CadetBlue2")
        title_lbl = tk.Label(profile_window, 
                            text = "Profile:", 
                            font = ("Helvetica", 15),
                            bg = "CadetBlue2")
        exit = tk.Button(profile_window,
                        text = "Exit",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = exit_profile) 
        profile_first_name_lbl = tk.Label(profile_window, 
                                            text = (f"First name: {first_name}"), 
                                            font = ("Helvetica", 11))
        profile_last_name_lbl = tk.Label(profile_window, 
                                            text = (f"Last name: {last_name}"), 
                                            font = ("Helvetica", 11))
        profile_username_lbl = tk.Label(profile_window, 
                                        text = (f"Username: {username}"), 
                                        font = ("Helvetica", 11))
        profile_birthdate_lbl = tk.Label(profile_window, 
                                            text = (f"Birthdate: {birthdate}"), 
                                            font = ("Helvetica", 11))
        profile_tertiary_status_lbl = tk.Label(profile_window, 
                                                text = (f"Tertiary status: {tertiary_status_words}"), 
                                                font = ("Helvetica", 11))
        profile_knowledge_lbl = tk.Label(profile_window, 
                                            text = (f"Knowledge of budgeting: {knowledge_words}"), 
                                            font = ("Helvetica", 11))
        signout_btn = tk.Button(profile_window,
                                text = "Signout", 
                                width = 7,
                                height = 1,
                                fg = "black",
                                bg = "firebrick1",
                                command = signout)
    
        # Place window content.
        canvas.place(x = 0, y = 20)
        title_lbl.place(x = 10, y = 34)
        exit.place(x = 200, y = 27)
        signout_btn.place(x = 120, y = 315)
        profile_first_name_lbl.place(x = 20, y = 100)
        profile_last_name_lbl.place(x = 20, y = 130)
        profile_username_lbl.place(x = 20, y = 160)
        profile_birthdate_lbl.place(x = 20, y = 190)
        profile_tertiary_status_lbl.place(x = 20, y = 220)
        profile_knowledge_lbl.place(x = 20, y = 250)

    # Function to open the about window.
    def open_about_window():

        # Function to exit profile page.
        def exit_about():
            response = messagebox.askquestion("Exit programme?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to exit the programme?", 
            icon = 'warning')
            print(response)
            if response == "yes":
                confirm_btn = Button(about_window, 
                                    command = about_window.quit)
                confirm_btn.pack()
                about_window.destroy()

        # Create about page.
        global about_window
        about_window = tk.Tk()
        about_window.geometry("1200x750")
        about_window.title("About")
        about_window.resizable(False, False)

        underlined_font = font.Font(size = 9, underline = True)

        # Create window content.
        title = tk.Label(about_window, 
                         text = "About this program:",
                         font = ("Helvetica", 40))
        canvas = Canvas(about_window, 
                        height = 100, 
                        width = 1210, 
                        bg = "CadetBlue2")
        home_btn = tk.Button(about_window,
                            text = "Home",
                            width = 10,
                            height = 2,
                            bg = "darkgrey",
                            command = about_to_main)
        open_about_btn = tk.Button(about_window,
                        text = "About",
                        font = underlined_font,
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey")
        open_budget_btn = tk.Button(about_window,
                        text = "My Budget",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey")
        open_tips_btn = tk.Button(about_window,
                        text = "Tips",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = tips_message)
        open_help_btn = tk.Button(about_window,
                        text = "Help",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "darkgrey",
                        command = about_to_help)
        profile_btn = tk.Button(about_window,
                        text = "Profile",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = open_profile)
        exit = tk.Button(about_window,
                        text = "Exit",
                        width = 10,
                        height = 2,
                        fg = "black",
                        bg = "grey",
                        command = exit_about)

        # Place labels, buttons, and images in a position.
        title.place(x = 200, y = 150)
        canvas.place(x = 0, y = 20)
        home_btn.place(x = 50, y = 40)
        open_about_btn.place(x = 244, y = 40)
        open_budget_btn.place(x = 438, y = 40)
        open_tips_btn.place(x = 632, y = 40)
        open_help_btn.place(x = 826, y = 40)
        profile_btn.place(x = 1020, y = 40)
        exit.place(x = 1110, y = 40)
        start_btn.place(x = 800, y = 290)

        about_window.mainloop()

    # Function to take the user from home page to help page.
    def home_to_help():
        home_window.destroy()
        open_help_window()

    # Function to take the user from home page to income page.
    def home_to_income():
        home_window.destroy()
        open_my_income()

    # Function to take the user from home page to about page.
    def home_to_about():
        home_window.destroy()
        open_about_window()

    # Function to take the user from help page to about page.
    def help_to_about():
        help_window.destroy()
        open_about_window()

    # Function to take the user from about page to help page.
    def about_to_help():
        about_window.destroy()
        open_help_window()

    # Function to take the user from income page to help page.
    def income_to_help():
        response = messagebox.askquestion("Exit my income?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to go help page?", 
        icon = 'warning')
        print(response)
        if response == "yes":
            confirm_btn = Button(income_window, 
                                command = income_window.quit)
            confirm_btn.pack()
            income_window.destroy()
            open_help_window()

    # Function to take the user from income page to about page.
    def income_to_about():
        response = messagebox.askquestion("Exit my income?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to go about page?", 
        icon = 'warning')
        print(response)
        if response == "yes":
            confirm_btn = Button(income_window, 
                                command = income_window.quit)
            confirm_btn.pack()
            income_window.destroy()
            open_about_window()

    # Function to take the user from expenses page to income page.
    def expenses_to_income():
        expenses_window.destroy()
        open_my_income()

    # Function to take the user from expenses page to about page.
    def expenses_to_about():
        response = messagebox.askquestion("Exit my income?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to go about page?", 
        icon = 'warning')
        print(response)
        if response == "yes":
            confirm_btn = Button(expenses_window, 
                                command = expenses_window.quit)
            confirm_btn.pack()
            expenses_window.destroy()
            open_about_window()

    # Function to take the user from expenses page to help page.
    def expenses_to_help():
        response = messagebox.askquestion("Exit my income?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to go help page?", 
        icon = 'warning')
        print(response)
        if response == "yes":
            confirm_btn = Button(expenses_window, 
                                command = expenses_window.quit)
            confirm_btn.pack()
            expenses_window.destroy()
            open_help_window()

    # Create home page.
    global home_window
    home_window = tk.Tk()
    home_window.geometry("1200x750")
    home_window.title("Home")
    home_window.resizable(False, False)

    underlined_font = font.Font(size = 9, underline = True)

    # Create window content.
    program_title = tk.Label(home_window,
        text = "Tertiary Budget \nTracker             ",
        font = ("Helvetica", 48))
    canvas = Canvas(home_window, 
                    height = 100, 
                    width = 1210, 
                    bg = "CadetBlue2")
    home_btn = tk.Button(home_window,
                        text = "Home",
                        font = underlined_font,
                        width = 10,
                        height = 2,
                        bg = "darkgrey")
    open_about_btn = tk.Button(home_window,
                    text = "About",
                    width = 10,
                    height = 2,
                    fg = "black",
                    bg = "darkgrey",
                    command = home_to_about)
    open_budget_btn = tk.Button(home_window,
                    text = "My Budget",
                    width = 10,
                    height = 2,
                    fg = "black",
                    bg = "darkgrey")
    open_tips_btn = tk.Button(home_window,
                    text = "Tips",
                    width = 10,
                    height = 2,
                    fg = "black",
                    bg = "darkgrey",
                    command = tips_message)
    open_help_btn = tk.Button(home_window,
                    text = "Help",
                    width = 10,
                    height = 2,
                    fg = "black",
                    bg = "darkgrey",
                    command = home_to_help)
    start_btn = tk.Button(home_window,
                            text = "Get started!",
                            width = 15,
                            height = 2,
                            font = ("Helvetica", 20),
                            bg = "gold",
                            command = home_to_income)
    profile_btn = tk.Button(home_window,
                    text = "Profile",
                    width = 10,
                    height = 2,
                    fg = "black",
                    bg = "grey",
                    command = open_profile)
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

    # Place labels, buttons, and images in a position.
    program_title.place(x = 200, y = 250)
    canvas.place(x = 0, y = 20)
    label1.place(x = 0, y = 450)
    home_btn.place(x = 50, y = 40)
    open_about_btn.place(x = 244, y = 40)
    open_budget_btn.place(x = 438, y = 40)
    open_tips_btn.place(x = 632, y = 40)
    open_help_btn.place(x = 826, y = 40)
    profile_btn.place(x = 1020, y = 40)
    exit.place(x = 1110, y = 40)
    start_btn.place(x = 800, y = 290)

    home_window.mainloop()

# Function to redirect user to the main code via help window.
def help_to_main():
    help_window.destroy()
    open_main_code()


# Function to redirect user to the main code via income window.
def income_to_main():
    income_window.destroy()
    open_main_code()

# Function to redirect user to the main code via about window.
def about_to_main():
    about_window.destroy()
    open_main_code()

# Function to redirect user to the main code via income window.
def expenses_to_main():
    response = messagebox.askquestion("Exit my expenses?","Your progress will " +
                                            "NOT be saved.\nAre you sure you want " +
                                            "to go home page?", 
    icon = 'warning')
    print(response)
    if response == "yes":
        confirm_btn = Button(expenses_window, 
                            command = expenses_window.quit)
        confirm_btn.pack()
        if 'expenses_window' in globals():
            expenses_window.destroy()
            open_main_code()

# Start the application.
open_first_window()