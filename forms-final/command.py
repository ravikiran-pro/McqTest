from Workbook import*
from locker import*
from random import randint
from datetime import date
from datetime import datetime
import tkinter
import os
class Command:
	def __init__(self,root,window):
		self.locker=Locker()
		self.root=root
		self.window=window	
	def destroy(self):
		self.root.destroy()
		self.window.destroy()
	def destroy_frame(self):
		self.root.destroy()
	def user_personal_data(self,name,college,department,year,location,mobile,email):	
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		self.row=self.workbook.size(self.book,"Student_data")
		book=self.workbook.copy_workbook(self.book)
		self.sheet=self.workbook.get_sheet(book,"Student_data")
		list=[str(date.today()),name,college,department,year,location,mobile,email]
		for i in range(len(list)):
			if i is 1 or i is 7:
				color=2
			else:
				color=1
			self.workbook.write_sheet(self.sheet,self.row,i,list[i],color)	
		self.workbook.save(book)
	def retrieve_data(self,filename):
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		self.row=self.workbook.size(self.book,filename)
		return self.row
	def generator(self,rows,question_count):
		data=[]
		for i in range(question_count):
			n=randint(1,rows-1)
			while n in data:
				n=randint(1,rows-1)
			data.append(n)
		return data
	def retrieve_data1(self,filename,data):
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		self.sheet=self.workbook.sheet(self.book,filename)
		list=[]
		list=self.workbook.read_sheet(data,self.sheet)
		return list
	def start(self):
		self.start = datetime.now()
	def score(self,choice,root,frame):
		self.root=root
		self.choice=choice
		self.frame=frame
		self.end=datetime.now()
		marks=0
		for j in range(len(self.choice)):
			choice_org=self.choice[j].var1.get()
			answer_org=self.choice[j].answer
			if answer_org==choice_org:
				marks+=1
			answer=""
			choice=""
		self.locker.openlocker()
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		self.row=self.workbook.size(self.book,"Student_data")
		book=self.workbook.copy_workbook(self.book)
		self.sheet=self.workbook.get_sheet(book,"Student_data")
		color=1
		self.workbook.write_sheet(self.sheet,self.row-1,8,str(self.end-self.start)[:8],color)	
		if int(marks)>14:
			color=0
		else:
			color=3
		self.workbook.write_sheet(self.sheet,self.row-1,9,marks,color)
		self.workbook.save(book)
		self.locker.closelocker()
		self.frame.destroy()
		self.root.destroy()


		
		

		