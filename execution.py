import tkinter
import tkinter as tk
window = tkinter.Tk()

window.title ("Login Form")
window.configure(bg = '#333333')
window.title("An image to present after logging in")

icon = tk.PhotoImage(file = "pearl.png")
label = tk.Label(window, image = icon)
label.pack()

window.mainloop()
