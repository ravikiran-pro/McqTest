from command import*
from locker import*
from test import*
class Append:
	def __init__(self,root,frame):
		self.root=root
		self.frame=frame
		self.c=Command(self.root,self.frame)
	def start(self,Name,Age,College,Department,Year,Location,Mobile,Email):
		self.locker = Locker()
		self.locker.openlocker()
		if Name.get() and College.get() and Department.get() and Year.get() and Location.get() and Mobile.get() and Email.get():
			self.c.user_personal_data(Name.get(),College.get(),Department.get(),Year.get(),Location.get(),Mobile.get(),Email.get())
			department=Department.get()
			question_count=15
			data=[]
			total=[]
			self.c.destroy_frame()
			c = Command(self.root,self.frame)
			list=["B.E ComputerScience","B.E Electrical and ELectronics","B.E Information Technology","B.E Electronics and Communication"
			,"B.Sc ComputerScience","B.C.A Computer Application","M.C.A Computer Application","M.Sc Computer Science","B.Sc Electronics","Others"]
			if(department == "B.E Electrical and ELectronics"):
				domain="Electrical"
			elif(department == "B.E Electronics and Communication" or department == "B.Sc Electronics"):
				domain="Electronics"
			else:
				domain="Computer"
			rows=c.retrieve_data("Aptitude") #row from command
			data=c.generator(rows,6)#column arrangement decoration
			for i in data:
				total.append(c.retrieve_data1("Aptitude",i))
	
			rows=c.retrieve_data("General") #row from command
			data=c.generator(rows,6)#column arrangement decoration
			for i in data:
				total.append(c.retrieve_data1("General",i))
	
			rows=c.retrieve_data(domain) #row from command
			data=c.generator(rows,15)#column arrangement decoration
			for i in data:
				total.append(c.retrieve_data1(domain,i))
	
	
			rows=c.retrieve_data("Networking") #row from command
			data=c.generator(rows,3)#column arrangement decoration
			for i in data:
				total.append(c.retrieve_data1("Networking",i))
			self.locker.closelocker()
			New_frame(department,total)
		else:
			messagebox.showerror("Retry","All fields are mandatory*")
			return 0
		