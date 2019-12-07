import tkinter as tk
class Window:
	def __init__(self):
		self.root=tk.Tk()
	def __geometry__(self,width,height):
		self.screen_width=self.root.winfo_screenwidth()
		self.screen_height=self.root.winfo_screenheight()
		dimenison = str(width)+'x'+str(height)
		self.root.geometry(dimenison)
		self.root.resizable(False,False)
	def __background__(self,color):
		self.color=color
		self.root.configure(background=color)
	def __start__(self):
		self.root.mainloop()
	def __title__(self,heading):
		self.root.title(heading)
	def __frame__(self):
		self.frame=tk.Frame(self.root,width=1000)
		return self.frame
	def resize(self):
		self.root.resizable(True,True)
	def target(self):
		print("target succesfull")

class Frame:
	def __init__(self,root):
		self.root=root
		self.frame=tk.Frame(self.root)
	def create(self):
		return self.frame
	def new(self):
		if self.frame is None:
			print("yes")
			return self.frame