import random
import string

testglobal = 'vinay'

class Myclassotp:
	result = ""
	"This class is for a OTP operations"
#rawotp = '0123456789!@$&#%abcdefghijklmnopqrstuvwxyz?+' -string.printable
#OTP = random.sample(rawotp,6)

	def otp(self,x):
		#result = ''
		for var in random.sample(string.printable,x):
			self.result=self.result+var
		print("Global variable print from class: ", testglobal)
		return self.result
	
in1 = int(input("Enter the length of OTP required: "))

obj1 = Myclassotp()

obj1.otp(in1)
print(obj1.otp(in1))
print ("This is the end of my code")
