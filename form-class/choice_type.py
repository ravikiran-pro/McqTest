from window import*
from GUI import*
from tkinter import ttk
from command import*

win = Window()
win.__geometry__(380,580)
win.__title__("Add Question")
frame=win.__frame__()
redirect =Command(frame,win.root)
"""Label new file"""
label1=Label(frame)
label1.text("Enter File")
label1.create()
label1.label.grid(row=0,column=0,sticky="w",padx="10")
"""Entry 	-new file"""
filepath=Entry(frame)
filepath.dimension(53,0,1)
filepath.create()
filepath.entry.grid(sticky="w",padx="10")
"""Button  -new file"""
new_file=Button(frame)
new_file.text("Create")
new_file.command(lambda: redirect.create_sheet(filepath.entry))
new_file.create()
new_file.button.grid(sticky="w",padx="10")
"""Label -question"""

label2=Label(frame)
label2.text("Enter Question")
label2.create()
label2.label.grid(sticky="w",padx="10")
"""Text -Question"""
Question=Text(frame)
Question.text("Enter Answer")
Question.dimension(40,5,1)
Question.create()
Question.text.grid(sticky="w",padx="10")

"""Label -question"""
label3=Label(frame)
label3.text("Choice1:")
label3.create()
label3.label.grid(sticky="w",padx="10")
"""Entry Answers"""
Choice1=Entry(frame)
Choice1.dimension(53,0,1)
Choice1.create()
Choice1.entry.grid(sticky="w",padx="10",ipady="2")

"""Label -question"""
label4=Label(frame)
label4.text("Choice2")
label4.create()
label4.label.grid(sticky="w",padx="10")
"""Entry Answers"""
Choice2=Entry(frame)
Choice2.dimension(53,0,1)
Choice2.create()
Choice2.entry.grid(sticky="w",padx="10",ipady="2")

"""Label -question"""
label5=Label(frame)
label5.text("Choice3")
label5.create()
label5.label.grid(sticky="w",padx="10")
"""Entry Answers"""
Choice3=Entry(frame)
Choice3.dimension(53,0,1)
Choice3.create()
Choice3.entry.grid(sticky="w",padx="10",ipady="2")

"""Label -question"""
label6=Label(frame)
label6.text("Choice4")
label6.create()
label6.label.grid(sticky="w",padx="10")
"""Entry Answers"""
Choice4=Entry(frame)
Choice4.dimension(53,0,1)
Choice4.create()
Choice4.entry.grid(sticky="w",padx="10",ipady="2")

"""Label -question"""
label7=Label(frame)
label7.text("Enter Answer")
label7.create()
label7.label.grid(sticky="w",padx="10")
"""Entry Answers"""
Answer=Entry(frame)
Answer.dimension(53,0,1)
Answer.create()
Answer.entry.grid(sticky="w",padx="10",ipady="2")
"""Button Create"""
create=Button(frame)
create.text("SUBMIT")
create.dimension(10,0,4)
create.command(lambda: redirect.multi_write_sheet(filepath.entry,Question.text
	,Choice1.entry,Choice2.entry,Choice3.entry,Choice4.entry,Answer.entry))

create.create()
create.button.grid(row="16",column="0",pady="30",sticky="w",padx="80")
"""Button exit"""
exit=Button(frame)
exit.text("EXIT")
exit.dimension(10,0,3)
exit.command(lambda: redirect.destroy())
exit.create()
exit.button.grid(row="16",column="0",sticky="w",padx="200")

frame.pack(side="left",fill="both",expand="true")
win.__start__()
