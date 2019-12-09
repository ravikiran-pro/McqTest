import tkinter as tk
import tkinter.font as font
from tkinter import ttk
"""Class Button  --parent class"""
class Button:
	def __init__(self,root):
		self.root=root
		"""Default properties"""
		font=Font(self.root,family="Consolas",size="12")
		self.font=font.create()
		self.width=0
		self.height=0
		self.border=1
		self.bg="white"
		self.fg="black"
	def text(self,text):
		self.text=text
	def dimension(self,width,height,border):
		self.width=width
		self.height=height
		self.border=border
	def color(self,bg,fg):
		self.bg=bg
		self.fg=fg
	def command(self,choice):
		self.command=choice
	def create(self):
		self.button = tk.Button(self.root,
			text=self.text,command=self.command,
			width=self.width,height=self.height,font=self.font,
			border=self.border,bg=self.bg,fg=self.fg)
	def capture(self,location):
		self.background=Background(self.root,location)
		self.image=tk.Button(self.root,image=self.background.photo,command=self.command,width=self.width,height=self.height)

"""class label"""
class Label(Button):
	def __init__(self,root):
		Button.__init__(self,root)
	def create(self):
		self.label=tk.Label(self.root,text=self.text,
			width=self.width,height=self.height,font=self.font
			,border=self.border,bg=self.bg,fg=self.fg)
	def capture(self,location):
		self.background=Background(self.root,location)
		self.image=tk.Label(self.root,image=self.background.photo,width=self.width)
"""class entry"""
class Checkbutton:
	def __init__(self,root):
		self.root=root
	def values(self,choice1,choice2,choice3,choice4,answer):
		self.choice1=choice1
		self.choice2=choice2
		self.choice3=choice3
		self.choice4=choice4
		self.answer=answer
		self.var1=tk.StringVar()
		self.var1.set(" ")
	def create(self):
		self.c1=tk.Checkbutton(self.root,text=self.choice1,variable=self.var1,offvalue="0",onvalue=self.choice1)
		self.c2=tk.Checkbutton(self.root,text=self.choice2,variable=self.var1,offvalue="0",onvalue=self.choice2)
		self.c3=tk.Checkbutton(self.root,text=self.choice3,variable=self.var1,offvalue="0",onvalue=self.choice3)
		self.c4=tk.Checkbutton(self.root,text=self.choice4,variable=self.var1,offvalue="0",onvalue=self.choice4)
class Entry(Button):
	def __init__(self,root):
		Button.__init__(self,root)
		self.width=40
	def create(self):
		self.entry=tk.Entry(self.root,text=self.text,
			width=self.width,
			border=self.border,font=self.font,	
			bg=self.bg, fg=self.fg)
class Text(Button):
		"""docstring for Text"""
		def __init__(self,root):
			Button.__init__(self,root)
		def create(self):
			self.text=tk.Text(self.root,
				width=self.width,height=self.height,
				border=self.border,font=self.font,
				bg=self.bg, fg=self.fg)		
class Font:
	def __init__(self,root,family,weight="normal",size=12,color="black"):
		self.root=root
		self.family=family
		self.size=size
		self.color=color
		self.weight=weight
	def create(self):
		self.myfont = tk.font.Font(self.root,family=self.family,
				size=self.size,weight=self.weight)
		return self.myfont

class Combobox(Button):
	def __init__(self,root):
		Button.__init__(self,root)
	def create(self,w,h,*product):
		self.combobox=ttk.Combobox(self.root,value=product,width=w,height=h,font=self.font)

class Background:
	def __init__(self,root,location):
		self.root=root;
		self.location=location
		self.photo=tk.PhotoImage(file=location)
		

	


		

		
