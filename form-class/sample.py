from tkinter import *
def answer(*list):
	print(list[0].get(),list[1].get())

master = Tk()
var1 = StringVar()
var1.set("0")
var2 = StringVar()
Checkbutton(master, text="male", variable=var1,onvalue="ravikiran").grid(row=0, sticky=W)
Checkbutton(master, text="female", variable=var1,onvalue="aurukiran").grid(row=1, sticky=W)
Checkbutton(master, text="female", variable=var1,onvalue="burukiran").grid(row=2, sticky=W)
Checkbutton(master, text="female", variable=var1,onvalue="curukiran").grid(row=3, sticky=W)
Checkbutton(master, text="female", variable=var1,onvalue="durukiran").grid(row=4, sticky=W)
Checkbutton(master, text="female", variable=var1,onvalue="eurukiran").grid(row=5, sticky=W)
Button(master,text="val",command=lambda:answer(var1,var2)).grid()
mainloop()
