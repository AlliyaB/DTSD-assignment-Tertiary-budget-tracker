import tkinter as tk

window = tk.Tk()
frame_a = tk.Frame()
label_a = tk.Label(master = frame_a, relief = tk.RAISED, text = "I am in frame a")
label_a.pack()

frame_b = tk.Frame()
label_b = tk.Label(master = frame_b, relief = tk.RAISED, text = "I am in frame b")
label_b.pack()

frame_a.pack()
frame_b.pack()
window.mainloop()