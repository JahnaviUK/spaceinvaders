from tkinter import *
root = Tk()
root.title ("restaurant management system")
root.geometry("500x400")


fries = StringVar()
burger = StringVar()
drinks = StringVar()
total = StringVar()


def calculate():
    f = int(fries.get()or 0)
    b = int(burger.get()or 0)
    d = int(drinks.get()or 0)

    total_cost = f*25 +b*40 +d*20
    tax = total_cost*0.05
    total.set("rs"+ str(round(total_cost + tax,2)))
def reset():
    fries.set("")
    burger.set("")
    drinks.set("")
    total.set("")
def exit_app():
    root.destroy()
Label(root,text ="restaurant management",font =("Arial",18,"bold"),fg ="tomato").pack(pady = 10)
frame = Frame(root)
frame.pack(pady = 10)
Label(frame,text = "fries (rs25)").grid(row = 0,column = 0,padx = 10,pady = 5)
Entry(frame,textvariable=fries).grid(row = 0,column = 1)


Label(frame,text = "burger (rs40)").grid(row = 1,column = 0,padx = 10,pady = 5)
Entry(frame,textvariable=burger).grid(row = 1,column = 1)

Label(frame,text = "drinks (rs20)").grid(row = 2,column = 0,padx = 10,pady = 5)
Entry(frame,textvariable=drinks).grid(row = 2,column = 1)
Label(root,text ="total cost").pack()
Entry(root,textvariable=total,font = ("Arial",14),width = 15,justify = "center").pack(pady = 5)
Button(root,text="calculate",bg = "lightgreen",width = 10,command = calculate).pack(side = LEFT,padx = 20,pady=20)
Button(root,text="reset",bg = "lightblue",width = 10,command = reset).pack(side = LEFT,padx = 20)
Button(root,text="exit",bg = "lightcoral",width = 10,command = exit_app).pack(side = LEFT,padx = 20)
root.mainloop()