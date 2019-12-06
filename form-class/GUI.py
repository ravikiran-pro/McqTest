import tkinter as tk
import tkinter.font as font
from tkinter import ttk
"""Class Button  --parent class"""
class Button:
	def __init__(self,root):
		self.root=root
		"""Default properties"""
		font=Font(self.root,family="helevetica",size="12",color="orange")
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

"""class label"""
class Label(Button):
	def __init__(self,root):
		Button.__init__(self,root)
	def create(self):
		self.label=tk.Label(self.root,text=self.text,
			width=self.width,height=self.height,font=self.font
			,border=self.border,bg=self.bg,fg=self.fg)
"""class entry"""
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
		f=Font(self.root,"helevetica","bold",12,"green")
		self.f=f.create()
	def create(self,w,h,*product):
		self.combobox=ttk.Combobox(self.root,value=product,width=w,height=h,font=self.f,background="green")


