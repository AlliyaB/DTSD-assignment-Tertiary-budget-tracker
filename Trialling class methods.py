# Imports each and every method and class 
# of module tkinter and tkinter.ttk
from tkinter import *
from tkinter.ttk import *

class GFG:
	def __init__(self, master = None):
		self.master = master

		# Calls create method of class GFG
		self.create()

	def create(self):

		# This creates a object of class canvas
		self.canvas = Canvas(self.master)

		# This creates a line of length 200 (straight horizontal line)
		self.canvas.create_line(15, 25, 200, 25)

		# This creates a lines of 300 (straight vertical dashed line)
		self.canvas.create_line(300, 35, 300, 200, dash = (5, 2))
		
		# This creates a triangle (triangle can be created by other methods also)
		self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
		
		# This pack the canvas to the main window and make it expandable
		self.canvas.pack(fill = BOTH, expand = True)

if __name__ == "__main__":
	
	# object of class Tk, responsible for creating
	# a tkinter toplevel window
	master = Tk()
	geeks = GFG(master)

	# This sets the title to Lines
	master.title("Lines")

	# This sets the geometry and position of window
	# on the screen
	master.geometry("400x250")

	# Infinite loop breaks only by interrupt
	master.mainloop()
