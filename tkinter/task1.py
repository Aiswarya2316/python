import tkinter

app = tkinter.Tk()

app.title("synnefo")
app.minsize(400,400)
app.maxsize(600,600)
app.config(bg="red")
l1=tkinter.Label(app,text="welcome",bg="red",fg="blue")
l1.pack()
e1=tkinter.Entry(app)
e1.pack()
b1=tkinter.Button(app,text="save",bg="black",fg="white",activebackground="green",activeforeground="red",padx=10,pady=10)
b1.pack()
app.mainloop()