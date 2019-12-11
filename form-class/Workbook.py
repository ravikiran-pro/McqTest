from xlutils.copy import copy	
from tkinter import messagebox
import random
import xlrd 	
import xlwt		

path="C:\\Users\\admin\\workspace\\files\\workbook.xls"
class Workbook:
	def open_workbook(self):
		global path
		book = xlrd.open_workbook(path,formatting_info=True)
		return book
	def copy_workbook(self,rb):
		book=copy(rb)
		return book
	def size(self,book,sheetname):
		try:
			sheet=book.sheet_by_name(sheetname)
			sheet.cell_value(0, 0)
			return sheet.nrows 		

		except xlrd.biffh.XLRDError:	
			messagebox.showerror("Service stopped","Improper Sheetname")
	def sheet(self,book,sheetname):
		sheet=book.sheet_by_name(sheetname)
		return sheet
	def new_sheet(self,book,filename):
		try:
			sheet = book.add_sheet(filename)
			sheet = book.get_sheet(filename)
			messagebox.showinfo("success","success")
			return sheet
		except:
			messagebox.showerror("Error",filename+" already present")
	def get_sheet(self,book,filename):
		sheet = book.get_sheet(filename)
		return sheet
	def read_sheet(self,row,sheet):
		list=[]
		list.append(sheet.cell(row,0).value)
		list.append(sheet.cell(row,1).value)
		list.append(sheet.cell(row,2).value)
		list.append(sheet.cell(row,3).value)
		list.append(sheet.cell(row,4).value)
		list.append(sheet.cell(row,5).value)
		return list
	def write_sheet(self,sheet,r1,c1,text1):
		sheet.write(r1,c1,text1.title())
	def save(self,book):
		global path
		book.save(path)
		
		

