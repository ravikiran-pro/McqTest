from tkinter import*
def mouse_wheel(event):
    global count
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        count -= 1
    if event.num == 4 or event.delta == 120:
        count += 1
    label['text'] = count
   
class scrollbar_implement:
	def __init__(self,root,RWidth,RHeight):
		self.root=root
		self.root.geometry("%dx%d+%d+%d"%(RWidth,RHeight-100,0,0))
		self.container = Frame(root)
		#Creating a canvas frame for adding Scrollbar
		self.canvas = Canvas(self.container,height=RHeight-120,width=RWidth-50)
		self.yscrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
		self.xscrollbar = Scrollbar(self.root, orient="horizontal", command=self.canvas.xview ,width=800)
		self.scrollable_frame = Frame(self.canvas)
		"""self.scrollable_frame.bind("<MouseWheel>", mouse_wheel)"""
		self.scrollable_frame.bind(
    	"<Configure>",
    	lambda e: self.canvas.configure(
	        scrollregion=self.canvas.bbox("all")
    	)
		)
		self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
		self.canvas.configure(yscrollcommand=self.yscrollbar.set)
		self.canvas.configure(xscrollcommand=self.xscrollbar.set)
	def create(self):
		return self.scrollable_frame
	def packing(self):
		self.container.pack()
		self.canvas.pack(side="left", fill="both", expand=True)
		self.yscrollbar.pack(side="right", fill="y")
		self.xscrollbar.pack(side="bottom", fill="x")
