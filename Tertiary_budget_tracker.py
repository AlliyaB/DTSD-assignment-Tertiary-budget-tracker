# Import tkinter.
import tkinter as tk
from tkinter import  *
import tkinter.font as tkFont
from tkinter import messagebox

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
program_title.pack(padx = 200, pady = 300)

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

# Create exit button and provide a message asking if the user is sure.
def popup():
  response=messagebox.askquestion("Title of message box ","Exit Programe ?", 
  icon='warning')
  print(response)
  if   response == "yes":
      b2=Button(r,text=("click here to exit"),command=r.quit)
      b2.pack()
  else:
    b2=Button(root,text="Thank you for selecting no for exit .")
    b2.pack()
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

# Create 
first_window.mainloop()

first_window.destroy()