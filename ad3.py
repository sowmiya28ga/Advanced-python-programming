from tkinter import *

root = Tk()
root.title("BCA App - Arithmetic Operations")
root.geometry("500x400")
root.config(bg="#e6f2ff")

Label(root, text="✨ ARITHMETIC OPERATIONS ✨", bg="#4da6ff", fg="white",
      font=("Arial Rounded MT Bold", 20)).pack(fill=X, pady=10)

f = Frame(root, bg="#cce6ff")
f.pack(pady=20)

Label(f, text="First Number:", bg="#cce6ff").grid(row=0, column=0, padx=10, pady=5)
n1 = Entry(f, width=20)
n1.grid(row=0, column=1)

Label(f, text="Second Number:", bg="#cce6ff").grid(row=1, column=0, padx=10, pady=5)
n2 = Entry(f, width=20)
n2.grid(row=1, column=1)

res = Label(root, text="", bg="#e6f2ff", fg="#003366", font=("Calibri", 14, "bold"))
res.pack(pady=15)

def calc(op):
    try:
        a, b = float(n1.get()), float(n2.get())
        if op=="add": r=a+b
        elif op=="sub": r=a-b
        elif op=="mul": r=a*b
        elif op=="div": r=a/b if b!=0 else "∞"
        res.config(text=f"Result: {r}")
    except: res.config(text="Enter valid numbers!")

for (t, c, o) in [("Add","green","add"),("Sub","red","sub"),
                  ("Mul","orange","mul"),("Div","blue","div")]:
    Button(root, text=t, bg=c, fg="white", width=8,
           font=("Arial",12,"bold"), command=lambda o=o: calc(o)).pack(side=LEFT, padx=10, pady=10)

root.mainloop()
