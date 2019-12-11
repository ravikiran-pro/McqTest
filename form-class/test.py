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
	win.__geometry__(screen_height,screen_width)
	scrollbar=scrollbar_implement(win.root,screen_height,screen_width)
	frame=scrollbar.create()
	frame.configure(background="#ffffff")
	redirect=Command(win.root,frame)
	choices=[]
	labels=[]
	col_row=7
	"""side label"""	
	banner = Label(frame)

	banner.color("white","black")
	banner.capture("images\\livewire.png")
	banner.dimension(33,22,0)
	banner.image.grid(row=1,padx=screen_height-300,pady=5,sticky="w")
	"""side label"""
	"""Head label"""
	header=Label(frame)
	header.capture("images\\header.png")
	header.image.grid(row=3,padx=screen_width/2+50,pady=20,sticky="w")
	"""Head label"""
	screen_width-=200
	mark=0
	for i in range(len(data)):
		label=Label(frame)
		label.text(str(mark+1)+")  "+data[i][0])
		mark+=1
		label.color("white","black")
		label.create(size=16)
		label.label.grid(row=col_row,padx=screen_width/2,sticky="w",pady=5)	
		choice=Checkbutton(frame)
		choice.values(data[i][1],data[i][2],data[i][3],data[i][4],data[i][5])
		choice.create()
		col_row+=1
		choice.c1.grid(row=col_row,padx=screen_width/2+100,sticky="w")
		choice.c2.grid(row=col_row,padx=screen_width/2+500,sticky="w")
		col_row+=1
		choice.c3.grid(row=col_row,padx=screen_width/2+100,sticky="w")
		choice.c4.grid(row=col_row,padx=screen_width/2+500,sticky="w")
		col_row+=1
		choices.append(choice)
	submit=Button(frame)
	submit.text("Start")
	submit.dimension(7,3,0)
	submit.command(lambda: redirect.score(choices,win.root,frame))
	submit.color("black","white")
	submit.create()
	submit.button.grid(row=col_row,padx=screen_width/2+300,sticky="w")
	win.__lockscreen__()
	scrollbar.packing()
	win.__start__()