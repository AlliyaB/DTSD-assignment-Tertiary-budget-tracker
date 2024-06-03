from tkinter import *
from tkinter.ttk import *

def process_name():
    """Do something with the name (in this case just print it)"""

    global name_entry # this will print hi {name} to terminal.
    print("Hi {}".format(name_entry.get()))

    global nameLabel # to change'the label with hi{name} text below the button.
    nameLabel.configure(text=f'Hi {name_entry.get()}')

    
    

def main():
    """Set up the GUI and run it"""

    global name_entry, nameLabel
    window = Tk()
    
    name_label = Label(window, text='Enter a name below:')
    name_label.grid(row=0, column=0)
    name_entry = Entry(window)
    name_entry.grid(row=1, column=3)
    button = Button(window, text='Say hello', command=process_name, padding=10)
    button.grid(row=1, column=0, columnspan=2)

    # I defined a label BELOW the button to show how to change
    nameLabel = Label(window, text=' ') # an empty text Label
    nameLabel.grid(row=2)
 
    window.mainloop()

        
main()