from window import*
from GUI import*
from command import*
from sample import scrollbar_implement

def New_frame(department):
	win = Window()
	win.__title__("Test")
	screen_height=win.screen_height()
	screen_width=win.screen_width()
	win.__geometry__(screen_height,screen_width)
	scrollbar=scrollbar_implement(win.root,screen_height,screen_width)
	frame=scrollbar.create()

	

	###Retrieve data
	###Selection box
	###Selection box
	win.__lockscreen__()
	scrollbar.packing()
	win.__start__()