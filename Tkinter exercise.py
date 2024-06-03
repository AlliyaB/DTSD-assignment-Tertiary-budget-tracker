import tkinter as tk 

window = tk.Tk()
ent = tk.Entry(width = 40,
               fg = "black",
               bg = "white"
)
ent.pack()
ent.insert(0, "What is your name? ")
window.mainloop()
