import tkinter
from Workbook import*
from locker import*
class Command:
	def __init__(self,root,window):
		self.locker=Locker()
		self.root=root
		self.window=window	
	def destroy(self):
		self.root.destroy()
	def create_sheet(self,sheetname):
		self.locker.openlocker()
		filename=sheetname.get()
		self.workbook = Workbook()
		self.book=self.workbook.open_workbook()
		book=self.workbook.copy_workbook(self.book)
		sheet=self.workbook.new_sheet(book,filename)
		messagebox.showinfo("success","success")
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
			self.workbook.write_sheet(self.sheet,self.row,0,question,self.row,1,answer)
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
			self.workbook.write_sheet(self.sheet,self.row,0,question,self.row,1,answer)
			self.workbook.write_sheet(self.sheet,self.row,2,choice1,self.row,3,choice2)
			self.workbook.write_sheet(self.sheet,self.row,4,choice3,self.row,5,choice4)
			self.workbook.save(book)
			messagebox.showinfo("success","success")
		self.locker.closelocker()