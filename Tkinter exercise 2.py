import tkinter as tk

window = tk.Tk()

frm_1 = tk.Frame(master = window, width = 100, height = 100, bg = "purple")
frm_1.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

lbl_1 = tk.Label(master = frm_1, text = "Im at (0,0)")
lbl_1.pack(x = 0, y = 0)

frm_2 = tk.Frame(master = window, width = 50, height = 50, bg = "blue")
frm_2.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)
lbl_2 = tk.Label(master = frm_2, text = "Im at (75, 75)", fg = "white", bg = "black")
lbl_2.pack(x = 75, y = 75)

frm_3 = tk.Frame(master = window, width = 25, height = 25, bg = "yellow")
frm_3.pack(fill = tk.BOTH, side = tk.LEFT, expand = True)

window.mainloop()