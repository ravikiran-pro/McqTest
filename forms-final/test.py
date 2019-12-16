from window import*
from GUI import*
from command import*
from scrollbar import scrollbar_implement
import os
def New_frame(department,data):
	win = Window()
	win.__title__("Test")
	screen_height=win.screen_height()
	screen_width=win.screen_width()
	win.__geometry__(screen_width,screen_height)
	scrollbar=scrollbar_implement(win.root,screen_height,screen_width)
	frame=scrollbar.create()
	frame.configure(background="#ffffff")
	redirect=Command(win.root,frame)
	redirect.start()
	choices=[]
	labels=[]
	col_row=6
	bal="                                                                                                                                                                                                                                                                                                                                             "
	print(bal)
	"""side label"""	
	banner = Label(frame)

	banner.color("white","black")
	banner.capture("images\\livewire.png")
	banner.dimension(50,22,0)
	banner.image.grid(row=1,padx=screen_height-(screen_height*20//100),pady=5,sticky="w")
	"""side label"""
	"""Head label"""
	header=Label(frame)
	header.capture("images\\header.png")
	header.image.grid(row=3,padx=screen_height*19//100,pady=50,sticky="w")
	"""Head label"""

	screen_width-=200
	mark=0
	for i in range(len(data)):
		"""Empty label"""
		col_row+=1
		label=Label(frame)
		label.text("  ")
		label.create()
		label.label.grid(row=col_row,padx=screen_height*3//100,sticky="w")
		"""Empty label"""
		col_row+=1
		if screen_height >= 1150: 
			w=80
			size=16
		elif screen_height > 1000:
			w=70
			size=14
		else:
			w=70
			size=12
		total_count=0
		count=0
		q=""
		start=0
		mark+=1
		if len(data[i][0]) > w and len(data[i][0]) > w+10:
			for l in data[i][0]:
				total_count+=1
				count+=1
				q+=l
				if count>w and l is ' ' or total_count == len(data[i][0]):
					if start is 0:
						question=str(mark)+") "+q
						start+=1
						q=""
					elif(mark<10):
						question=str("   "+q)
					else:
						question=str("    "+q)
					label=Label(frame)
					label.text(question.title())
					label.color("silver","green")
					label.create(size)
					col_row+=1
					label.label.grid(row=col_row,padx=screen_height*3//100,sticky="w")
					count=0
					q=""
		else:
			label=Label(frame)
			label.text(str(mark)+")  "+data[i][0])
			label.color("silver","green")
			label.create(size)
			label.label.grid(row=col_row,padx=screen_height*3//100,sticky="w")
		col_row+=1
		label=Label(frame)
		label.text("  ")
		label.dimension(400,1,0)
		label.create()
		label.label.grid(row=col_row,padx=screen_height*3//100,sticky="w")
		"""Empty label"""
		choice=Checkbutton(frame)
		choice.values(data[i][1],data[i][2],data[i][3],data[i][4],data[i][5])
		choice.create()
		col_row+=1
		choice.c1.grid(row=col_row,padx=screen_height*12.1//100,sticky="w")
		choice.c2.grid(row=col_row,padx=screen_height*54.8//100,sticky="w")
		"""Empty label"""
		col_row+=1
		label=Label(frame)
		label.text("  ")
		label.create()
		label.label.grid(row=col_row,padx=screen_height//10,sticky="w")
		"""Empty label"""
		col_row+=1
		choice.c3.grid(row=col_row,padx=screen_height*12.1//100,sticky="w")
		choice.c4.grid(row=col_row,padx=screen_height*54.8//100,sticky="w")
		col_row+=1
		choices.append(choice)
	submit=Button(frame)
	submit.text("Start")
	#submit.dimension(150,60,0)
	submit.command(lambda: redirect.score(choices,win.root,frame))
	submit.capture("images\\submit.png")
	submit.image.grid(row=col_row,padx=screen_height*43.8//100,sticky="w",pady="40")
	"""Empty label"""
	label=Label(frame)
	label.text("  ")
	label.create()
	label.label.grid(row=col_row+1,padx=screen_height*43.8//100,sticky="w")
	"""Empty label"""
	win.__lockscreen__()
	scrollbar.packing()
	win.__start__()