from tkinter import *
route = Tk()
route.title("number pad")
route.geometry("250x300")
frame = Frame(master = route,height = 200,width = 360,bg = "yellow")
nums = [[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    route.columnconfigure(i,weight = 1,minsize = 75)
    route.rowconfigure(i,weight = 1,minsize = 50)
    for j in range (0,3):
        frame = Frame(master = route,relief=SUNKEN,borderwidth = 1)
        frame.grid(row = i,column = j)
        label = Label(master = frame,text = nums[i][j],bg="light blue")
        label.pack(padx = 3,pady = 3)
route.mainloop()