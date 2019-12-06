from window import*
from GUI import*
from tkinter import ttk
from command import*

win = Window()
win.__geometry__(340,380)
win.__title__("start")
frame=win.__frame__()
redirect =Command(frame,win.root)

"""label 	-Name"""
label1=Label(frame)
label1.text("Name")
label1.create()
label1.label.grid(row=0,column=0,sticky="w",padx="10")
"""label 	-age"""
label2=Label(frame)
label2.text("Age")
label2.create()
label2.label.grid(row=0,column=0,sticky="w",padx="250")
"""Entry 	-Name"""
Name=Entry(frame)
Name.dimension(22,0,1)
Name.create()
Name.entry.grid(row=1,column=0,sticky="w",padx="10")
"""Entry  -age"""
Age=Entry(frame)
Age.dimension(7,0,1)
Age.create()
Age.entry.grid(row=1,column=0,sticky="w",padx="250")
"""Entry 	-Name"""
label3=Label(frame)
label3.text("College name")
label3.create()
label3.label.grid(row=2,sticky="w",padx="10")
"""Entry  -age"""
College=Entry(frame)
College.dimension(34,0,1)
College.create()
College.entry.grid(row=3,sticky="w",padx="10")
"""label 	-department"""
label4=Label(frame)
label4.text("Department")
label4.create()
label4.label.grid(row=4,column=0,sticky="w",padx="10")
"""label 	-year"""
label5=Label(frame)
label5.text("Year")
label5.create()
label5.label.grid(row=4,column=0,sticky="w",padx="250")
"""DropDown 	-department"""
Department=Combobox(frame)
list=["B.E Mechanical Engineering","B.E Production Engineering","B.E ComputerScience Engineering","B.E Civil Engineering","B.E ELectrical Engineering"]
Department.create(20,3,*list)
Department.combobox.grid(row=5,column=0,sticky="w",padx="10")
"""DropDown 	-department"""
Year=Combobox(frame)
list=["Ist yr","IInd yr","IIIrd yr","IVth yr","passed-out"]
Year.create(5,5,*list)
Year.combobox.grid(row=5,column=0,sticky="w",padx="250")
"""label -location"""
label6=Label(frame)
label6.text("Location")
label6.create()
label6.label.grid(row=6,column=0,sticky="w",padx="10",pady="10")
"""Entry -location"""
Location=Entry(frame)
Location.dimension(26,0,1)
Location.create()
Location.entry.grid(row=6,column=0,sticky="w",padx="85",pady="10")
"""label -Email"""
label7=Label(frame)
label7.text("Email id")
label7.create()
label7.label.grid(row=7,column=0,sticky="w",padx="10",pady="10")
"""Entry -Email"""
Mobile=Entry(frame)
Mobile.dimension(26,0,1)
Mobile.create()
Mobile.entry.grid(row=7,column=0,sticky="w",padx="85",pady="10")
"""label -Email"""
label8=Label(frame)
label8.text("Mobile")
label8.create()
label8.label.grid(row=8,column=0,sticky="w",padx="10",pady="10")
"""Entry -Email"""
Email=Entry(frame)
Email.dimension(26,0,1)
Email.create()
Email.entry.grid(row=8,column=0,sticky="w",padx="85",pady="10")

labelr=Label(frame)
labelr.create()
labelr.label.p = tk.PhotoImage(file="images\\drop_down.png")
labelr.label.grid()

frame.pack(side="left",fill="both",expand="true")
win.__start__()
