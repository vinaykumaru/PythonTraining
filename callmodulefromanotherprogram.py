package = "apache"

def work():
	print("working from Home")

class NoWork(object):
	def __init__(self,name,state):
		self.name = name
		self.state = state		
	
	def work_or_nowork(self):
		print("I am"+self.name+"and I am"+self.state)
		

import callmodulefromanotherprogram

print 
