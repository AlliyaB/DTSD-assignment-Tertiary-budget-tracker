import tkinter as tk

window = tk.Tk()
# Display label.
label = tk.Label(
    text = "Hello! Welcome to my interface.",
    height = 30,
    width = 110,
    fg = "blue", # Set the text colour.
    bg = "white" # Set the background colour
)
label.pack()

# Display label name and get input from user.
label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()
# Retrieve the users name and assign it to the variable 'name'.
name = entry.get()
name

# Display label welcoming user by name.
label = tk.Label(
    text = f"Hello {name}! Welcome to my interface.", 
    fg = "purple",
    bg = "white"
)
label.pack()

# Display button.
button = tk.Button(
    text = "Click me!",
    width = 25,
    height = 5,
    fg = "white",
    bg = "blue"
)
button.pack()
window.mainloop()

window.destroy()