from tkinter import *
route = Tk()
route.title("login app")
route.geometry("400x400")
frame = Frame(master = route,height = 200,width = 360,bg = "yellow")
lbl1 = Label(frame,text = "full name",bg = "pink",fg = "white",width = 12)
lbl2 = Label(frame,text = "email ID",bg = "pink",fg = "white",width = 12)
lbl3 = Label(frame,text = "enter password",bg = "pink",fg = "white",width = 12)
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame)
def display():
    name = name_entry.get()
    greet = "hey "+ name
    message = " congrats for ur new account"
    textbox.insert(END,greet)
    textbox.insert(END,message)
textbox = Text(bg = "purple",fg = "white")
btn = Button(text = "create an account",command = display,bg = "red")
frame.place(x = 20,y = 0)
lbl1.place(x = 20,y = 20)
name_entry.place(x = 150,y = 20)
lbl2.place(x = 20,y = 80)
email_entry.place(x = 150,y = 80)
lbl3.place(x = 20,y = 140)
frame.place(x = 20,y = 0)
pass_entry.place(x = 150,y = 140)
btn.place(x = 130,y = 210)
frame.place(x = 20,y = 0)
textbox.place(y = 250)
btn.place(x = 130,y = 210)
route.mainloop()










