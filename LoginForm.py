from tkinter import *

import tkinter as tk
import tkinter.messagebox
window = tk.Tk()
window.title ("Login Form")
window.geometry("800x300")
window.configure(bg = '#333333')

#execfile to another python script

#Account Validation:
def login():
    username = "1"
    password = "1"
    if user_entry.get()==username and password_entry.get()==password:
        tkinter.messagebox.showinfo("Login Successfully", "Success!")  
        frame.destroy()
        window.title ("Login Form")
        window.geometry("1024x1024")

        window.configure(bg = '#333333')

        window.title("An image to present after logging in")

        icon = tk.PhotoImage(file = "pearl.png")
        label = tk.Label(window, image = icon)
        label.pack()
        window.mainloop()
    else:
        tkinter.messagebox.showinfo("Invalid Credentials", "Invalid Username or Password")

#Show Password Function
def show_password():

    if password_entry.cget('show') =='•':
        password_entry.config(show = '')
    else:
        password_entry.config(show = '•')
    
       
frame = tk.Frame (bg = '#333333')
#widgets
login_label = tk.Label(frame, text = "Login", bg ='#333333', fg = '#ffffff', font = ("Arial", 24))
user_label = tk.Label(frame, text = "Username", bg ='#333333', fg = '#ffffff')
user_entry = tk.Entry(frame)
password_label = tk.Label(frame, text = "Password", bg ='#333333', fg = '#ffffff')
password_entry = tk.Entry(frame, show="•")
login_button = tk.Button(frame, text = "login", bg ='#337333', fg = '#ffffff',width = 15, command = login)
check_button = tk.Checkbutton(frame, text = "Show Password", bg ='#333333', fg = '#ffffff', command = show_password)

#Styling
login_label.grid(row = 0, column = 0, columnspan = 2, pady = 40)
user_label.grid(row = 1, column = 0)
user_entry.grid(row = 1, column = 1)
password_label.grid(row = 2, column = 0)
password_entry.grid(row = 2, column = 1)
login_button.grid (row = 4, column = 1, columnspan = 2)
check_button.grid (row = 3, column = 1)
frame.pack()
window.mainloop()
