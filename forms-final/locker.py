from Workbook import path as location
from os import remove as rem
from os import system as sys
from os import chdir as cdc
from os import getcwd as cd
from subprocess import call as EXEC
class Locker:
	def __init__(self):
		path=cd()
		self.path=path
		self.opath=self.path+"\\openlock.bat"
		self.cpath=self.path+"\\closelock.bat"
		self.openlock=[b'\xff\xfe\x00\x00@\x00\x00\x00E\x00\x00\x00C\x00\x00\x00H\x00\x00\x00O\x00\x00\x00 \x00\x00\x00O\x00\x00\x00F\x00\x00\x00F\x00\x00\x00\n\x00\x00\x00', b'\xff\xfe\x00\x00a\x00\x00\x00t\x00\x00\x00t\x00\x00\x00r\x00\x00\x00i\x00\x00\x00b\x00\x00\x00 \x00\x00\x00-\x00\x00\x00h\x00\x00\x00 \x00\x00\x00-\x00\x00\x00s\x00\x00\x00 \x00\x00\x00"\x00\x00\x00C\x00\x00\x00o\x00\x00\x00n\x00\x00\x00t\x00\x00\x00r\x00\x00\x00o\x00\x00\x00l\x00\x00\x00 \x00\x00\x00P\x00\x00\x00a\x00\x00\x00n\x00\x00\x00e\x00\x00\x00l\x00\x00\x00.\x00\x00\x00{\x00\x00\x002\x00\x00\x001\x00\x00\x00E\x00\x00\x00C\x00\x00\x002\x00\x00\x000\x00\x00\x002\x00\x00\x000\x00\x00\x00-\x00\x00\x003\x00\x00\x00A\x00\x00\x00E\x00\x00\x00A\x00\x00\x00-\x00\x00\x001\x00\x00\x000\x00\x00\x006\x00\x00\x009\x00\x00\x00-\x00\x00\x00A\x00\x00\x002\x00\x00\x00D\x00\x00\x00D\x00\x00\x00-\x00\x00\x000\x00\x00\x008\x00\x00\x000\x00\x00\x000\x00\x00\x002\x00\x00\x00B\x00\x00\x003\x00\x00\x000\x00\x00\x003\x00\x00\x000\x00\x00\x009\x00\x00\x00D\x00\x00\x00}\x00\x00\x00"\x00\x00\x00\n\x00\x00\x00', b'\xff\xfe\x00\x00r\x00\x00\x00e\x00\x00\x00n\x00\x00\x00 \x00\x00\x00"\x00\x00\x00C\x00\x00\x00o\x00\x00\x00n\x00\x00\x00t\x00\x00\x00r\x00\x00\x00o\x00\x00\x00l\x00\x00\x00 \x00\x00\x00P\x00\x00\x00a\x00\x00\x00n\x00\x00\x00e\x00\x00\x00l\x00\x00\x00.\x00\x00\x00{\x00\x00\x002\x00\x00\x001\x00\x00\x00E\x00\x00\x00C\x00\x00\x002\x00\x00\x000\x00\x00\x002\x00\x00\x000\x00\x00\x00-\x00\x00\x003\x00\x00\x00A\x00\x00\x00E\x00\x00\x00A\x00\x00\x00-\x00\x00\x001\x00\x00\x000\x00\x00\x006\x00\x00\x009\x00\x00\x00-\x00\x00\x00A\x00\x00\x002\x00\x00\x00D\x00\x00\x00D\x00\x00\x00-\x00\x00\x000\x00\x00\x008\x00\x00\x000\x00\x00\x000\x00\x00\x002\x00\x00\x00B\x00\x00\x003\x00\x00\x000\x00\x00\x003\x00\x00\x000\x00\x00\x009\x00\x00\x00D\x00\x00\x00}\x00\x00\x00"\x00\x00\x00 \x00\x00\x00f\x00\x00\x00i\x00\x00\x00l\x00\x00\x00e\x00\x00\x00s\x00\x00\x00']
		self.closelock=[b'\xff\xfe\x00\x00@\x00\x00\x00E\x00\x00\x00C\x00\x00\x00H\x00\x00\x00O\x00\x00\x00 \x00\x00\x00O\x00\x00\x00F\x00\x00\x00F\x00\x00\x00\n\x00\x00\x00', b'\xff\xfe\x00\x00r\x00\x00\x00e\x00\x00\x00n\x00\x00\x00 \x00\x00\x00f\x00\x00\x00i\x00\x00\x00l\x00\x00\x00e\x00\x00\x00s\x00\x00\x00 \x00\x00\x00"\x00\x00\x00C\x00\x00\x00o\x00\x00\x00n\x00\x00\x00t\x00\x00\x00r\x00\x00\x00o\x00\x00\x00l\x00\x00\x00 \x00\x00\x00P\x00\x00\x00a\x00\x00\x00n\x00\x00\x00e\x00\x00\x00l\x00\x00\x00.\x00\x00\x00{\x00\x00\x002\x00\x00\x001\x00\x00\x00E\x00\x00\x00C\x00\x00\x002\x00\x00\x000\x00\x00\x002\x00\x00\x000\x00\x00\x00-\x00\x00\x003\x00\x00\x00A\x00\x00\x00E\x00\x00\x00A\x00\x00\x00-\x00\x00\x001\x00\x00\x000\x00\x00\x006\x00\x00\x009\x00\x00\x00-\x00\x00\x00A\x00\x00\x002\x00\x00\x00D\x00\x00\x00D\x00\x00\x00-\x00\x00\x000\x00\x00\x008\x00\x00\x000\x00\x00\x000\x00\x00\x002\x00\x00\x00B\x00\x00\x003\x00\x00\x000\x00\x00\x003\x00\x00\x000\x00\x00\x009\x00\x00\x00D\x00\x00\x00}\x00\x00\x00"\x00\x00\x00\n\x00\x00\x00', b'\xff\xfe\x00\x00a\x00\x00\x00t\x00\x00\x00t\x00\x00\x00r\x00\x00\x00i\x00\x00\x00b\x00\x00\x00 \x00\x00\x00+\x00\x00\x00h\x00\x00\x00 \x00\x00\x00+\x00\x00\x00s\x00\x00\x00 \x00\x00\x00"\x00\x00\x00C\x00\x00\x00o\x00\x00\x00n\x00\x00\x00t\x00\x00\x00r\x00\x00\x00o\x00\x00\x00l\x00\x00\x00 \x00\x00\x00P\x00\x00\x00a\x00\x00\x00n\x00\x00\x00e\x00\x00\x00l\x00\x00\x00.\x00\x00\x00{\x00\x00\x002\x00\x00\x001\x00\x00\x00E\x00\x00\x00C\x00\x00\x002\x00\x00\x000\x00\x00\x002\x00\x00\x000\x00\x00\x00-\x00\x00\x003\x00\x00\x00A\x00\x00\x00E\x00\x00\x00A\x00\x00\x00-\x00\x00\x001\x00\x00\x000\x00\x00\x006\x00\x00\x009\x00\x00\x00-\x00\x00\x00A\x00\x00\x002\x00\x00\x00D\x00\x00\x00D\x00\x00\x00-\x00\x00\x000\x00\x00\x008\x00\x00\x000\x00\x00\x000\x00\x00\x002\x00\x00\x00B\x00\x00\x003\x00\x00\x000\x00\x00\x003\x00\x00\x000\x00\x00\x009\x00\x00\x00D\x00\x00\x00}\x00\x00\x00"\x00\x00\x00']
	def openlocker(self,c=1):
		base_dir=cd()
		with open(self.opath,"w") as obj:
			for i in self.openlock:
				obj.write(i.decode("utf-32"))
			obj.close()
		cdc(self.path)
		EXEC([r'openlock.bat'])
		rem(self.opath)
		cdc(base_dir)
	def closelocker(self):
		base_dir=cd()
		with open(self.cpath,"w") as obj:
			for i in self.closelock:
				obj.write(i.decode("utf-32"))
			obj.close()
		cdc(self.path)
		EXEC([r'closelock.bat'])
		rem(self.cpath)
		cdc(base_dir)

	

	