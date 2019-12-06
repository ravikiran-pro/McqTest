import tkinter as tk
class Window:
	def __init__(self):
		self.root=tk.Tk()
	def __geometry__(self,width,height):
		dimenison = str(width)+'x'+str(height)
		self.root.geometry(dimenison)
		self.root.resizable(0,0)
	def __start__(self):
		self.root.mainloop()
	def __title__(self,heading):
		self.root.title(heading)
	def __frame__(self):
		self.frame=tk.Frame(self.root)
		return self.frame