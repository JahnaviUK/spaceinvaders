from tkinter import *
from tkinter import messagebox
route = Tk()
route.title("denomination couter")
route.configure(bg = "light blue")
route.geometry("650x400")
lable1 = Label(route,text="hey user welcome to denomination counter application",bg = "light blue")
lable1.place(relx = 0.5,y = 340,anchor = CENTER)
def msg():
    msgbox = messagebox.showinfo("alert","do u want to calculate the denomination count")
    if msgbox == "ok":
        topwin()
button1 = Button(route,text = "lets get started",command = msg,bg = "brown",fg="white")
button1.place(x=260,y=360)
def topwin():
    top = Toplevel()
    top.title("denomination calculator")
    top.configure(bg = "light gray")
    top.geometry("600x350+50+50")
    label=Label(top,text = "enter total amount",bg = "light gray")
    entry = Entry(top)
    lbl=Label(top,text = "here are the number of notes for each denomination ",bg = "light gray")
    l1=Label(top,text="2000",bg = "light gray")
    l2=Label(top,text="500",bg = "light gray")
    l3=Label(top,text="100",bg = "light gray")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount//2000
            amount%=2000
            note500 = amount//500
            amount%=500
            note100=amount//100
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
            messagebox.showerror("error")
    btn = Button(top,text = "calculate",command = calculator,bg ="brown",fg = "white")
    label.pack()
    entry.pack()
    btn.pack()
    lbl.pack()
    l1.pack()
    l2.pack()
    l3.pack()
    t1.pack()
    t2.pack()
    t3.pack()
    top.mainloop()
route.mainloop()
        

