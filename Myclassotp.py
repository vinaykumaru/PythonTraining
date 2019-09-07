import random
import string
class Myclassotp:
	"This class is for a OTP operations"
	#rawotp = '0123456789!@$&#%abcdefghijklmnopqrstuvwxyz?+' -string.printable
	#OTP = random.sample(rawotp,6)

	def otpGenerator(self,x):
		ans = ''
		for var in random.sample(string.printable,x):
			ans=ans+var
		return ans
	
in1 = int(input("Enter the length of OTP required: "))

obj1 = Myclassotp()
obj2 = Myclassotp()

obj1.otpGenerator(in1)
print(obj1.otpGenerator(in1))
print ("This is the end of my code")
