from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("my first GUI")

btn1 = Button(window,text = "Click me I'm a VIRUS", fg = "White", bg = "Black")
btn1.place(x = 185, y = 200)
txt = Entry(window,border = 10)
txt.place(x = 180, y = 150)

lbl = Label(window,text = "My first demo", font = "Verdanna")
lbl.place(x= 190, y = 50)


window.mainloop()
