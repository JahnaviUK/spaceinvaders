from tkinter import *
from tkinter import messagebox 
route = Tk()
route.geometry("200x200")
def msg():
    messagebox.askretrycancel("alert","stop virus found")
button = Button(route,text = "scan for virus",command = msg)
button.place(x = 40,y = 80)
route.mainloop() 