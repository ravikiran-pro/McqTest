import tkinter
from command import*
from test import*
class Append:
	def __init__(self,root,frame):
		self.root=root
		self.frame=frame
		self.c=Command(self.root,self.frame)
	def start(self,Name,Age,College,Department,Year,Location,Mobile,Email):
		self.c.user_personal_data(Name.get(),College.get(),Department.get(),Year.get(),Location.get(),Mobile.get(),Email.get())
		department=Department.get()
		question_count=30
		data=[]
		c = Command(self.root,self.frame)
		rows=c.retrieve_data("programming")
		data=c.generator(rows,question_count)
		total=[]
		print(data)
		self.c.destroy_frame()
		New_frame(department)
		for i in data:
			total.append(c.retrieve_data1("programming",i))
		print(total)
