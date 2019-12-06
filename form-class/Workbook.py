from xlutils.copy import copy	
from tkinter import messagebox
import random
import os
import xlrd 	
import xlwt		

path="C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Python\\Python37\\include\\internal\\files\\workbook.xls"
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
	
	def new_sheet(self,book,filename):
		try:
			sheet = book.add_sheet(filename)
			sheet = book.get_sheet(filename)
			return sheet
		except:
			messagebox.showerror("Error",filename+" already present")
	def get_sheet(self,book,filename):
		sheet = book.get_sheet(filename)
		return sheet
	def write_sheet(self,sheet,r1,c1,text1,r2,c2,text2):
		sheet.write(r1,c1,text1)
		sheet.write(r2,c2,text2)
	def save(self,book):
		global path
		book.save(path)
		
		

