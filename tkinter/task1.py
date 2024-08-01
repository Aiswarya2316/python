import tkinter
from tkinter import messagebox
app = tkinter.Tk()
def data():
    # v=v1.get()
    # l2.config(text=v)
    messagebox.askokcancel("display",v1.get())

app.title("synnefo")
app.minsize(400,400)
app.maxsize(600,600)
app.config(bg="red")
l1=tkinter.Label(app,text="welcome",bg="red",fg="blue")
l1.pack()
v1=tkinter.StringVar()
e1=tkinter.Entry(app,textvariable=v1)
e1.pack()
b1=tkinter.Button(app,text="save",bg="black",fg="white",activebackground="green",activeforeground="red",padx=10,pady=10,command=data)
b1.pack()
l2=tkinter.Label(app)
l2.pack()
app.mainloop()