from tkinter import*
def mouse_wheel(event):
    global count
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        count -= 1
    if event.num == 4 or event.delta == 120:
        count += 1
    label['text'] = count
def scrolllistbox2(event):
    listbox2.yview_scroll(int(-1*(event.delta/120)), "units")
"""class scrollbar_implement:
	def __init__(self,root,RWidth,RHeight):
		root.geometry("%dx%d"%(RWidth,RHeight))
		root.resizable(0,0)	#non-re-sizable Window
		container = Frame(root)
		#Creating a canvas frame for adding Scrollbar
		canvas = Canvas(container,height=RHeight-50,width=RWidth-50)
		scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
		scrollable_frame = Frame(canvas)
		scrollable_frame.bind(
    	"<Configure>",
    	lambda e: canvas.configure(
	        scrollregion=canvas.bbox("all")
    	)
		)
		canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
		canvas.configure(yscrollcommand=scrollbar.set)
		for i in range(100):
			Label(scrollable_frame,text="dd").pack()
		
		container.pack()
		canvas.pack(side="left", fill="both", expand=True)
		scrollbar.pack(side="right", fill="y")"""
class scrollbar_implement:
	def __init__(self,root,RWidth,RHeight):
		self.root=root
		self.root.geometry("%dx%d"%(RWidth,RHeight))
		self.root.resizable(0,0)	#non-re-sizable Window
		self.container = Frame(root)
		#Creating a canvas frame for adding Scrollbar
		self.canvas = Canvas(self.container,height=RHeight-50,width=RWidth-50)
		self.scrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
		self.scrollable_frame = Frame(self.canvas)
		"""self.scrollable_frame.bind("<MouseWheel>", mouse_wheel)"""
		self.scrollable_frame.bind("<MouseWheel>", scrolllistbox2)
		self.scrollable_frame.bind(
    	"<Configure>",
    	lambda e: self.canvas.configure(
	        scrollregion=self.canvas.bbox("all")
    	)
		)
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)
	def create(self):
		return self.scrollable_frame
	def packing(self):
		self.container.pack()
		self.canvas.pack(side="left", fill="both", expand=True)
		self.scrollbar.pack(side="right", fill="y")