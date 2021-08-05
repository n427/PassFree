import tkinter as tk
from tkinter import PhotoImage
from ctypes import windll

''' Page Styling '''
# Initialize sizes
HEIGHT = 1000
WIDTH = 1200
root = tk.Tk()
online = "True"
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = "#D4D4CE")
frame.place(relx = 0.5, rely = 0.05, relheight = 0.9, relwidth = 0.9, anchor = "n")
windll.shcore.SetProcessDpiAwareness(1)

# Additions
colour_label = tk.Label(frame, bg = "#287094")
colour_label.place(rely = 0.55, relheight = 0.9, relwidth = 3, anchor = "n")


img = PhotoImage(file="PassFree.png")      
logo = tk.Label(frame, image = img, bg = "#D4D4CE")
logo.place(relx = 0.0000001, rely = 0.000001) 

sign_label = tk.Label(frame, bg = "#023246", fg = "white", text = "PassFree", font = ("Courier", 30), width = 12, height = 2)
sign_label.place(rely = 0.22, relx = 0.71)

''' Register '''
register_username_label = tk.Label(frame, text = "Username:", font = ("Courier", 20))
register_username_label.place(rely = 0.63, relx = 0.05)
register_username_entry = tk.Entry(frame, justify = "center", font = ("Courier", 20), width = 18)
register_username_entry.place(rely = 0.68, relx = 0.05, relheight = 0.05)

register_password_label = tk.Label(frame, text = "Password:", font = ("Courier", 20))
register_password_label.place(rely = 0.74, relx = 0.05)
register_password_entry = tk.Entry(frame, justify = "center", font = ("Courier", 20), width = 18, show = "*")
register_password_entry.place(rely = 0.79, relx = 0.05, relheight = 0.05)

user = " "
def createaccount():
    global user
    user = register_username_entry.get()
    account = open("users.txt", "a")
    open(register_username_entry.get() + ".txt", "x")
    account.write(register_username_entry.get() + " : ")
    account.write(register_password_entry.get() + "\n")

    print(user)
    root.destroy()
    return user
    
register_button = tk.Button(frame, takefocus=False, text = "Register", font =("Courier", 14), bg = "#023246", fg = "white", command = createaccount)
register_button.place(relx = 0.05, rely = 0.86, relwidth = 0.1, relheight = 0.05)


''' Login '''
username_label = tk.Label(frame, text = "Username:", font = ("Courier", 20))
username_label.place(rely = 0.63, relx = 0.5)
username_entry = tk.Entry(frame, justify = "center", font = ("Courier", 20), width = 18)
username_entry.place(rely = 0.68, relx = 0.5, relheight = 0.05)

password_label = tk.Label(frame, text = "Password:", font = ("Courier", 20))
password_label.place(rely = 0.74, relx = 0.5)
password_entry = tk.Entry(frame, justify = "center", font = ("Courier", 20), width = 18, show = "*")
password_entry.place(rely = 0.79, relx = 0.5, relheight = 0.05)

user = " "
f = open("users.txt", "r").read()
def login():
    global user
    user = username_entry.get()
    if username_entry.get() and password_entry.get() in f:  
        print(user)
        root.destroy()
    else:
        print("Wrong username / password")
    return user

login_button = tk.Button(frame, takefocus=False, text = "Login", font =("Courier", 14), bg = "#023246", fg = "white", command = login)
login_button.place(relx = 0.5, rely = 0.86, relwidth = 0.1, relheight = 0.05)


root.mainloop()