import tkinter as tk
from pathlib import Path


def login_verify():
    username = admin_username_verify.get()# get info from field
    password = admin_password_verify.get()# get info from field
    username_entry.delete("0", tk.END) # delete info after button press
    password_entry.delete("0", tk.END)# delete info after button press
    file = ("Existing Users.txt", "a")  # file name
    nothing = "" # use to check empty field

    if username != nothing and password != nothing: # check if the fields are empty
        if username in Path(file).read_text() and password in Path(file).read_text(): #use pathlib to open and check file contents
            print("Access Granted")
        else:
            print("Incorrect Username/Password combination")
    else:
        print("Invalid Credentials")


root = tk.Tk()
root.geometry("800x800")
root.title("Administrator Login")


admin_username_verify = tk.StringVar()
admin_password_verify = tk.StringVar()

login_label = tk.Label(root, text="Please enter details below to login", font="Times 12 bold")
login_label.pack()
user_name_label = tk.Label(root, text="Username *", font="Times 10 bold")
user_name_label.pack(pady=2)
username_entry = tk.Entry(root, textvariable=admin_username_verify, font="Times 12")
username_entry.pack()
password_label = tk.Label(root, text="Password *", font="Times 10 bold")
password_label.pack()
password_entry = tk.Entry(root, text=admin_password_verify, show="*", font="Times 12")
password_entry.pack()
login_button = tk.Button(root, text="Login", bg="blue", fg="white", width=10,
                         command= login_verify)
login_button.pack(pady=5)


root.mainloop()