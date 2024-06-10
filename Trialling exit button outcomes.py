# Import tkinter.
import tkinter as tk
from tkinter import  *
import tkinter.font as tkFont
from tkinter import messagebox

# Create a function to double check the user wants to exit before exiting.
def popup():
  response=messagebox.askquestion("Exit Programme?","Your progress will " +
                                  "NOT be saved.\nAre you sure you want " +
                                  "to exit the program?", 
  icon='warning')
  print(response)
  if response == "yes":
    confirm_btn = Button(first_window, command = first_window.quit)
    confirm_btn.pack()
    first_window.destroy()

# Create Log in/sign up window.
first_window = tk.Tk()
first_window.geometry("1200x750")
first_window.title("Log in/Sign up")
# Create fonts.
#roman_font = tkFont.Font(family = "Arial=", size = 40, slant = tkFont.ROMAN)
# Display label.
program_title = tk.Label(first_window,
    text = "Tertiary Budget \nTracker             ",
    font = ("Helvetica", 48),
)
program_title.place(x = 200, y = 250)

# Create a coloured box for the top where navigation bar will be.
canvas = Canvas(first_window, height = 100, width = 1210, bg = "BLUE", )
canvas.place(x = 0, y = 20)

# Signup and login button.
signup = tk.Button(first_window,
                   text = "Sign up",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "grey",
                   command = first_window.destroy
)

login = tk.Button(first_window,
                   text = "Log in",
                   width = 10,
                   height = 2,
                   fg = "black",
                   bg = "blue",
                   command = first_window.destroy
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
signup.place(x = 990, y = 40)
login.place(x = 900, y = 40)
exit.place(x = 1110, y = 40)

# Create labels informing the user about what the program does.
info_lbl_one = Label(first_window, text = "Enjoy a budget plan tailored to your financial wants and needs.")
info_lbl_one.place(x = 850, y = 500)

first_window.mainloop()

first_window.destroy()