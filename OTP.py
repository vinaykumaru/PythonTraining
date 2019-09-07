# Logic of OTP: 
'''import random
rawotp = '0123456789!@$&#%abcdefghijklmnopqrstuvwxyz+?'
OTP = random.sample(rawotp,8)
print(OTP)'''

# Program to generate OTP:

'''import random
in1 = int(input("Enter the length of OTP required: "))
rawotp = '0123456789!@$&#%abcdefghijklmnopqrstuvwxyz?+'
#OTP = random.sample(rawotp,x)

def otpGenerator(x):
	ans = ''
	for var in random.sample(rawotp,x):
		ans=ans+var
	return ans

test = otpGenerator(in1)
print("Your OTP is: ",test)'''



import random
import string
in1 = str(input("Press any key to receive your OTP: "))
rawotp = string.printable
#rawotp = '0123456789!@$&#%abcdefghijklmnopqrstuvwxyz?+'
OTP = random.sample(rawotp,6)

def otpGenerator(x):
	ans = ''
	for var in OTP:
		ans=ans+var
	return ans

test = otpGenerator(in1)
print("Your OTP is: ",test)



















	

	
