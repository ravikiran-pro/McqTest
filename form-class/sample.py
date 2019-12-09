from tkinter import *
def answer(*list):
	print(list[0].get(),list[1].get())

master = Tk()
var1 = StringVar()
var1.set("a")
var2 = StringVar()
Checkbutton(master, text="male", variable=var1,onvalue="ravikiran").grid(row=0, sticky=W)
Checkbutton(master, text="female", variable=var2,onvalue="gurukiran").grid(row=1, sticky=W)
Button(master,text="val",command=lambda:answer(var1,var2)).grid()
mainloop()
