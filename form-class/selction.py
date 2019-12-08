from window import*
from GUI import*
from tkinter import ttk
from command import*
from append_forms import*

win = Window()
win.__title__("Quest")
win.__geometry__(360,400)
win.__lockscreen__()
uniquebackground="tomato"
one=Frame(win.root)
frame=one.create()
frame.configure(background=uniquebackground)
redirect=Append(win.root,frame)

"""Creating bannner"""
banner=Label(frame)
banner.capture("images\\livewire.png")

"""label 	-imageborder"""
empty=Label(frame)
empty.text(" ")
empty.color(uniquebackground,"black")
empty.create()

"""label 	-Name"""
label1=Label(frame)
label1.text("Name")
label1.color(uniquebackground,"black")
label1.create()
"""label 	-age"""
label2=Label(frame)
label2.text("Age")
label2.color(uniquebackground,"black")
label2.create()
"""Entry 	-Name"""
Name=Entry(frame)
Name.dimension(22,0,1)
Name.create()
"""Entry  -age"""
Age=Entry(frame)
Age.dimension(7,0,1)
Age.create()
"""Entry 	-Name"""
label3=Label(frame)
label3.text("College name")
label3.color(uniquebackground,"black")
label3.create()
"""Entry  -age"""
College=Entry(frame)
College.dimension(35,0,1)
College.create()
"""label 	-department"""
label4=Label(frame)
label4.text("Department")
label4.color(uniquebackground,"black")
label4.create()
"""label 	-year"""
label5=Label(frame)
label5.text("Year")
label5.color(uniquebackground,"black")
label5.create()
"""DropDown 	-department"""
Department=Combobox(frame)
list=["B.E Mechanical Engineering","B.E Production Engineering","B.E ComputerScience Engineering","B.E Civil Engineering","B.E ELectrical Engineering"]
Department.create(20,3,*list)
"""DropDown 	-department"""
Year=Combobox(frame)
list=["Ist yr","IInd yr","IIIrd yr","IVth yr","passed-out"]
Year.create(5,5,*list)
"""label -location"""
label6=Label(frame)
label6.text("Location")
label6.color(uniquebackground,"black")
label6.create()
"""Entry -location"""
Location=Entry(frame)
Location.dimension(26,0,1)
Location.create()
"""label -Email"""
label7=Label(frame)
label7.text("Email id")
label7.color(uniquebackground,"black")
label7.create()
"""Entry -Email"""
Mobile=Entry(frame)
Mobile.dimension(26,0,1)
Mobile.create()
"""label -Email"""
label8=Label(frame)
label8.text("Mobile")
label8.color(uniquebackground,"black")
label8.create()
"""Entry -Email"""
Email=Entry(frame)
Email.dimension(26,0,1)
Email.create()
"""Button -start"""
submit=Button(frame)
submit.text("Start")
submit.dimension(70,30,0)
submit.command(lambda: redirect.start(Name.entry,Age.entry,College.entry,Department.combobox,Year.combobox,Location.entry,Mobile.entry,Email.entry))
submit.capture("images//button.png")

"""Packing Everything"""
banner.image.grid(row=0,column=0,sticky="w",pady="5",padx="95")
empty.label.grid(row=1,sticky="w")
label1.label.grid(row=6,column=0,sticky="w",padx="10")
label2.label.grid(row=6,column=0,sticky="w",padx="265")
Name.entry.grid(row=7,column=0,sticky="w",padx="10")
Age.entry.grid(row=7,column=0,sticky="w",padx="265")
label3.label.grid(row=8,sticky="w",padx="10")
College.entry.grid(row=9,sticky="w",padx="10")
label4.label.grid(row=10,column=0,sticky="w",padx="10")
label5.label.grid(row=10,column=0,sticky="w",padx="265")
Department.combobox.grid(row=11,column=0,sticky="w",padx="10")
Year.combobox.grid(row=11,column=0,sticky="w",padx="265")
label6.label.grid(row=12,column=0,sticky="w",padx="10",pady="10")
Location.entry.grid(row=12,column=0,sticky="w",padx="95",pady="10")
label7.label.grid(row=13,column=0,sticky="w",padx="10",pady="10")
Mobile.entry.grid(row=13,column=0,sticky="w",padx="95",pady="10")
label8.label.grid(row=14,column=0,sticky="w",padx="10",pady="10")
Email.entry.grid(row=14,column=0,sticky="w",padx="95",pady="10")
submit.image.grid(row=15,sticky="w",padx="130",pady="10")
frame.pack(side="left",expand="true")

if __name__ == '__main__':
	win.__start__()

