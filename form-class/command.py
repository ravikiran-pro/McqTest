import tkinter
from Workbook import*
from locker import*
from random import randint
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
	def create_sheet(self,sheetname):
		self.locker.openlocker()
		filename=sheetname.get()
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		book=self.workbook.copy_workbook(self.book)
		sheet=self.workbook.new_sheet(book,filename)
		try:
			self.workbook.write_sheet(sheet,0,0,"Question",0,1,"Answer")
		except:
			print("error")
		finally:
			self.workbook.save(book)
		self.locker.closelocker()
	def single_write_sheet(self,sheetname,Question,Answer):
		self.locker.openlocker()
		filename=sheetname.get()
		question=Question.get('1.0',tkinter.END)
		answer=Answer.get()
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		self.row=self.workbook.size(self.book,filename)
		book=self.workbook.copy_workbook(self.book)
		if self.row is not None:
			self.sheet=self.workbook.get_sheet(book,filename)
			self.workbook.write_sheet(self.sheet,self.row,0,question)
			self.workbook.write_sheet(self.sheet,self.row,1,answer)
			self.workbook.save(book)
			messagebox.showinfo("success","success")
		self.locker.closelocker()
	def multi_write_sheet(self,sheetname,Question,Choice1,Choice2,Choice3,Choice4,Answer):
		self.locker.openlocker()
		filename=sheetname.get()
		question=Question.get('1.0',tkinter.END)
		answer=Answer.get()
		choice1=Choice1.get()
		choice2=Choice2.get()
		choice3=Choice3.get()
		choice4=Choice4.get()
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		self.row=self.workbook.size(self.book,filename)
		book=self.workbook.copy_workbook(self.book)
		if self.row is not None:
			self.sheet=self.workbook.get_sheet(book,filename)
			list=[question,answer,choice1,choice2,choice3,choice4]
			for i in range(len(list)):
				self.workbook.write_sheet(self.sheet,self.row,i,list[i])	
		self.workbook.save(book)
		messagebox.showinfo("success","success")
		self.locker.closelocker()	
	def user_personal_data(self,name,college,department,year,location,mobile,email):	
		self.locker.openlocker()
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		self.row=self.workbook.size(self.book,"student_data")
		book=self.workbook.copy_workbook(self.book)
		self.sheet=self.workbook.get_sheet(book,"student_data")
		list=[name,college,department,year,location,mobile,email]
		for i in range(len(list)):
			self.workbook.write_sheet(self.sheet,self.row,i,list[i])	
		self.workbook.save(book)
		self.locker.closelocker()
	def retrieve_data(self,filename):
		self.locker.openlocker()
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
		self.locker.openlocker()
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		self.sheet=self.workbook.sheet(self.book,filename)
		list=[]
		list=self.workbook.read_sheet(data,self.sheet)
		self.locker.closelocker()
		return list
		

		