from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Student Mark List")
root.geometry("500x600")

l = Label(root, text="User Name", font=("Arial", 12))
l.pack(pady=10)


e = Entry(root, font=("Arial", 12))
e.pack(pady=5)


b = Button(root, text="Login")
b.pack(pady=10)

root.mainloop()

