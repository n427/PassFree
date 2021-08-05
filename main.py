import tkinter as tk
from tkinter import ttk, PhotoImage
import random 
from ctypes import windll
from login import *

''' Page Styling '''
# Initialize sizes
HEIGHT = 1000
WIDTH = 1200
root = tk.Tk()
root.title("PassFree")
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()
takefocus=False

frame = tk.Frame(root, bg = "#D4D4CE")
frame.place(relx = 0.5, rely = 0.05, relheight = 0.9, relwidth = 0.9, anchor = "n")
windll.shcore.SetProcessDpiAwareness(1)

# Create tabs
s = ttk.Style()
s.configure('TNotebook.Tab', font=('Courier','20','bold') )
tabs = ttk.Notebook(root)
tabs.place(relx = 0.5, rely = 0.05, relheight = 0.9, relwidth = 0.9, anchor = "n")

make = tk.Frame(tabs, frame)
access = tk.Frame(tabs, frame)
quit = tk.Frame(tabs, frame)

make.place()
access.place()
quit.place()

tabs.add(make, text = "           \n          Make          \n             ")
tabs.add(access, text = "          \n         Access        \n           ")
tabs.add(quit, text = "          \n         Quit          \n          ")

# Additions 
make_colour = tk.Label(make, bg = "#287094")
make_colour.place(rely = 0.55, relheight = 0.9, relwidth = 3, anchor = "n")
access_colour = tk.Label(access, bg = "#287094")
access_colour.place(rely = 0.55, relheight = 0.9, relwidth = 3, anchor = "n")
quit_colour = tk.Label(quit, bg = "#287094")
quit_colour.place(rely = 0.55, relheight = 0.9, relwidth = 3, anchor = "n")

img = PhotoImage(file="PassFree.png")      
make_logo = tk.Label(make, image = img, bg = "#D4D4CE")
make_logo.place(relx = 0.0000001, rely = 0.000001) 
access_logo = tk.Label(access, image = img, bg = "#D4D4CE")
access_logo.place(relx = 0.0000001, rely = 0.0000001) 
quit_logo = tk.Label(quit, image = img, bg = "#D4D4CE")
quit_logo.place(relx = 0.0000001, rely = 0.0000001) 

make_sign = tk.Label(make, bg = "#023246", fg = "white", text = "Make", font = ("Courier", 30), width = 12, height = 2)
make_sign.place(rely = 0.22, relx = 0.71)
access_sign = tk.Label(access, bg = "#023246", fg = "white", text = "Access", font = ("Courier", 30), width = 12, height = 2)
access_sign.place(rely = 0.22, relx = 0.71)
quit_sign = tk.Label(quit, bg = "#023246", fg = "white", text = "Quit", font = ("Courier", 30), width = 12, height = 2)
quit_sign.place(rely = 0.22, relx = 0.71)


''' Make page '''
# Website field 
website_label = tk.Label(make, text  = "Website Name:", fg = "black", font =("Courier", 20))
website_label.place(relx = 0.02, rely = 0.65)
website_entry = tk.Entry(make, font =("Courier", 20), justify = "center", width = 10)
website_entry.place(relx = 0.02, rely = 0.71)

# Animal field
animal_label = tk.Label(make, text  = "Animal:", fg = "black", font =("Courier", 20))
animal_label.place(relx = 0.02, rely = 0.79)
animal_entry = tk.Entry(make, font =("Courier", 20), justify = "center", width = 10)
animal_entry.place(relx = 0.02, rely = 0.85)

# Numbers field
numbers_label = tk.Label(make, text  = "Four Numbers:", fg = "black", font =("Courier", 20))
numbers_label.place(relx = 0.35, rely = 0.65)
numbers_entry = tk.Entry(make, font =("Courier", 20), justify = "center", width = 10)
numbers_entry.place(relx = 0.35, rely = 0.71)

# Colour field
colour_label = tk.Label(make, text  = "Colour:", fg = "black", font =("Courier", 20))
colour_label.place(relx = 0.35, rely = 0.79)
colour_entry = tk.Entry(make, font =("Courier", 20), justify = "center", width = 10)
colour_entry.place(relx = 0.35, rely = 0.85)

# Generate button
symbols = ["@", "!", "#", "$", "%", "^", "&", "*", "(", ")"]
def makePassword():
    global password
    password = animal_entry.get().title() + random.choice(symbols) + numbers_entry.get() + random.choice(symbols) + colour_entry.get().title()
    message = website_entry.get().title() + ":\n" + password
    password_created = tk.Label(make, text = message, font = ("Courier", 15), bg = "white", width = 21, height = 9, wraplength= 250, justify = "center")
    password_created.place(relx = 0.742, rely = 0.635)
    return password

generate_button = tk.Button(make, takefocus=False, text = "Generate", width = 10, height = 1, font =("Courier", 18), command = makePassword, bg = "#023246", fg = "white")
generate_button.place(relx = 0.54, rely = 0.75)
preview_label = tk.Label(make, bg = "white", width = 21, height = 9, text = "Password:", font = ("Courier", 15, "bold"))
preview_label.place(relx = 0.742, rely = 0.635)

# Save button
saved_passwords_text = tk.StringVar()
def save():
    save_pass = open(user + ".txt", "a")
    save_pass.write(website_entry.get().title() + " : ")
    save_pass.write(password + ",  ")
    save_pass.close()
    saved_pass = open(user + ".txt", "r")
    saved_passwords_text.set(saved_pass.read())
    saved_passwords = tk.Label(access, textvariable = saved_passwords_text, bg = "white", font = ("Courier", 15), height = 13, wraplength=700, justify="center")
    saved_passwords.place(relx = 0.5, relheight = 0.38, rely = 0.5845, relwidth = 0.96, anchor = "n")

save_button = tk.Button(make, takefocus=False, text = "Save", font =("Courier", 14), command = save, bg = "#D4D4CE")
save_button.place(relx = 0.877, rely = 0.925, relwidth = 0.1, relheight = 0.05)


''' Access Page '''
saved_passwords = tk.Label(access, textvariable = saved_passwords_text, bg = "white", font = ("Courier", 15), wraplength=700, justify="center")
saved_passwords.place(relx = 0.5, relheight = 0.38, rely = 0.5845, relwidth = 0.96, anchor = "n")

# Add website
prev_website_label = tk.Label(access, text  = "Website Name:", fg = "black", font =("Courier", 20))
prev_website_label.place(relx = 0.02, rely = 0.43)
prev_website_entry = tk.Entry(access, font =("Courier", 20), justify = "center", width = 13)
prev_website_entry.place(relx = 0.02, rely = 0.49)

# Add password
prev_password_label = tk.Label(access, text  = "Password:", fg = "black", font =("Courier", 20))
prev_password_label.place(relx = 0.25, rely = 0.43)
prev_password_entry = tk.Entry(access, font =("Courier", 20), justify = "center", width = 13)
prev_password_entry.place(relx = 0.25, rely = 0.49)


# Show previous entries
saved = open(user + ".txt", "r").read()
saved_passwords = tk.Label(access, text = saved, bg = "white", font = ("Courier", 15), height = 13, wraplength=700, justify="center")
saved_passwords.place(relx = 0.5, relheight = 0.38, rely = 0.5845, relwidth = 0.96, anchor = "n")

# Add new entries
def addprevPass():
    add_prev_pass = open(user + ".txt", "a")
    add_prev_pass.write(prev_website_entry.get().title() + " : ")
    add_prev_pass.write(prev_password_entry.get() + ",  ")
    add_prev_pass.close()
    saved_passes = open(user + ".txt", "r").read()
    saved_passwords_text.set(saved_passes)
    saved_passwords = tk.Label(access, textvariable = saved_passwords_text, bg = "white", font = ("Courier", 15), height = 13, wraplength=700, justify="center")
    saved_passwords.place(relx = 0.5, relheight = 0.38, rely = 0.5845, relwidth = 0.96, anchor = "n")

add_button = tk.Button(access, text = "Add", width = 10, height = 1, font =("Courier", 18), command = addprevPass, bg = "#023246", fg = "white")
add_button.place(relx = 0.5, rely = 0.46)



""" Quit Page """
# Leave application
def leave():
    root.destroy()

close_button = tk.Button(quit, takefocus = False, bg = "#023246", fg = "white", text = "Close Passfree", font = ("Courier", 15), width = 20, height = 3, command = leave)
close_button.place(rely = 0.63, relx = 0.5, anchor = "n")

# Clear passwords
def clear():
    open(user + ".txt", "w").close()
    saved_passwords = tk.Label(access, bg = "white", font = ("Courier", 15), height = 13, wraplength=700, justify="center")
    saved_passwords.place(relx = 0.5, rely = 0.5845, relwidth = 0.96, anchor = "n")

clear_button = tk.Button(quit, takefocus = False, bg = "#023246", fg = "white", text = "Clear Passwords", font = ("Courier", 15), width = 20, height = 3, command = clear)
clear_button.place(rely = 0.82, relx = 0.5, anchor = "n")

root.mainloop()