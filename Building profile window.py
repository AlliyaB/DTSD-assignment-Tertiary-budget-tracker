# Import tkinter.
import tkinter as tk
from tkinter import  *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Create building profile page, user will be directed here after signing up.
building_profile_window = tk.Tk()
building_profile_window.geometry("1200x750")
building_profile_window.title("Building my profile")
building_profile_window.resizable(False, False)

# Create a coloured box for the top where navigation bar will be.
canvas = Canvas(building_profile_window, height = 100, width = 1210, bg = "CadetBlue2", )
canvas.place(x = 0, y = 20)

# Display label.
program_title = tk.Label(building_profile_window,
    text = "Building my profile",
    font = ("Helvetica", 30),
    bg = "CadetBlue2"
)
program_title.place(x = 10, y = 40)

building_profile_window.mainloop()