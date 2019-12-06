from window import*
from GUI import*
from command import*

win = Window()
win.__geometry__(380,380)
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
label3.text("Enter Answer")
label3.create()
label3.label.grid(sticky="w",padx="10")
"""Entry Answers"""
Answer=Entry(frame)
Answer.dimension(53,0,1)
Answer.create()
Answer.entry.grid(sticky="w",padx="10",ipady="2")
"""Button Create"""
create=Button(frame)
create.text("SUBMIT")
create.dimension(10,0,4)
create.command(lambda: redirect.single_write_sheet(filepath.entry,Question.text,Answer.entry))
create.create()
create.button.grid(row="7",column="0",pady="30",sticky="w",padx="80")
"""Button exit"""
exit=Button(frame)
exit.text("EXIT")
exit.dimension(10,0,3)
exit.command(lambda: redirect.destroy())
exit.create()
exit.button.grid(row="7",column="0",sticky="w",padx="200")


"""
"packing"
label1.label.grid(row=0,column=0,sticky="w",padx="10")
filepath.entry.grid(sticky="w",padx="10")
new_file.button.grid(sticky="w",padx="10")
label2.label.grid(sticky="w",padx="10")
Question.text.grid(sticky="w",padx="10")
label3.label.grid(sticky="w",padx="10")
Answer.entry.grid(sticky="w",padx="10",ipady="2")
create.button.grid(row="7",column="0",pady="30",sticky="w",padx="80")
exit.button.grid(row="7",column="0",sticky="w",padx="200")
"packing"
"""
frame.pack(side="left",fill="both",expand="true")
win.__start__()

																												

