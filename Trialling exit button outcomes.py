from tkinter import  *
from tkinter import messagebox
root=Tk()
def clicked():
  label1=Label(root,text="This is text")
  label1.pack()
def popup():
  response=messagebox.askquestion("Title of message box ","Exit Programe ?", 
  icon='warning')
  print(response)
  if   response == "yes":
      b2=Button(root,text=("click here to exit"),command=root.quit)
      b2.pack()
  else:
    b2=Button(root,text="Thank you for selecting no for exit .")
    b2.pack()
button=Button(root,text="Button click",command=clicked)
button2=Button(root,text="Exit Programe ?",command=popup)
button.pack()
button2.pack()
root.mainloop()