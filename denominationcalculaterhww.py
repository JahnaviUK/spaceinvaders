from tkinter import *
from tkinter import messagebox
route = Tk()
route.title("denomination couter")
route.configure(bg = "light pink")
route.geometry("650x400")
lable1 = Label(route,text="hey user welcome to denomination counter application",bg = "light pink")
lable1.place(relx = 0.5,y = 340,anchor = CENTER)
def msg():
    msgbox = messagebox.showinfo("alert","do u want to calculate the denomination count")
    if msgbox == "ok":
        topwin()
button1 = Button(route,text = "lets get started",command = msg,bg = "purple",fg="light blue")
button1.place(x=260,y=360)
def topwin():
    top = Toplevel()
    top.title("denomination calculator")
    top.configure(bg = "light green")
    top.geometry("600x350+50+50")
    label=Label(top,text = "enter total amount",bg = "light green")
    entry = Entry(top)
    lbl=Label(top,text = "here are the number of notes for each denomination ",bg = "light gray")
    l1=Label(top,text="500",bg = "light gray")
    l2=Label(top,text="100",bg = "light gray")
    l3=Label(top,text="50",bg = "light gray")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note500 = amount//500
            amount%=500
            note100 = amount//100
            amount%=100
            note50=amount//50
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(note500))
            t2.insert(END,str(note100))
            t3.insert(END,str(note50))
        except ValueError:
            messagebox.showerror("error")
    btn = Button(top,text = "calculate",command = calculator,bg ="light purple",fg = "light blue")
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
        

