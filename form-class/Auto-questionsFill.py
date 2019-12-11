import xlrd
import xlwt
from xlutils.copy import copy	

path="C:\\Users\\admin\\workspace\\files\\workbook.xls"

def inputs(sheetname,*list):
	global path
	current=read_sheet_rows(sheetname,path)  
	if(current!=0):
		update_sheet_values(current,sheetname,*list) 

def read_sheet_rows(sheetname,filepath):
	global path
	book = xlrd.open_workbook(path)
	try:
		sheet=book.sheet_by_name(sheetname)
		sheet.cell_value(0, 0)
		return sheet.nrows 		

	except xlrd.biffh.XLRDError:	
		return 0

def update_sheet_values(current,sheetname,list):
	global path
	rb = xlrd.open_workbook(path)
	wb=copy(rb) 					
	sheet=wb.get_sheet(sheetname)
	sheet.write(current,0,list[0])	
	sheet.write(current,1,list[1])
	sheet.write(current,2,list[2])
	sheet.write(current,3,list[3])
	sheet.write(current,4,list[4]) 	
	sheet.write(current,5,list[int(list[5])]) 	
	wb.save(path)

with open("key.txt") as obj:
	count=0
	filename="Electrical"
	entire=[]
	for i in obj.readlines():
		entire.append(i)
		count+=1
		if(count is 6):
			inputs(filename,entire)
			count=0
			entire=[]


