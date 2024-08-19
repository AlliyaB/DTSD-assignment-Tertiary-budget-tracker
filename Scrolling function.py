# Python Program to make a scrollable frame
# using Tkinter

from tkinter import *

# create help_window window
help_window = Tk()
help_window.geometry("1200x750")

# create a vertical scrollbar-no need
# to write orient as it is by
# default vertical
scrollbar = Scrollbar(help_window)

# attach Scrollbar to help_window window on 
# the side
scrollbar.pack(side = RIGHT, fill = Y)

user_manual_file = open("User_manual.txt","r")
user_manual = user_manual_file.read()

# create a Text widget with 15 chars
# width and 15 lines height
# here xscrollcomannd is used to attach Text
# widget to the horizontal scrollbar
# here yscrollcomannd is used to attach Text
# widget to the vertical scrollbar
text_box = Text(help_window, width = 120, height = 37, wrap = NONE,
		# xscrollcommand = h.set, 
		yscrollcommand = scrollbar.set)

# insert some text into the text widget
text_box.insert(END, user_manual)

# attach Text widget to help_window window at top
text_box.pack(side = BOTTOM)

# here command represents the method to
# be executed yview is executed on
# object 't' Here t may represent any
# widget
scrollbar.config(command = text_box.yview)

help_window.mainloop()


