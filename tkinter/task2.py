import tkinter

app=tkinter.Tk()
c=tkinter.Canvas(app,width=400,height=400,bg="red")
c.create_line(0,150,250,150,fill="green")
c.create_rectangle(50,50,150,150,fill="black")
c.create_oval(50,50,150,150,fill="red")
c.pack()
app.mainloop()