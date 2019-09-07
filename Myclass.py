class Myclass:
	"This clss is for basic learning python"
	num = 10
	var = 2
	def fun1(self):
		print("Welcome message from fun1 of Myclass")
	
obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj4 = Myclass()

print(obj1.num**2)
print(obj1.__doc__)
obj1.fun1()
print (obj2.num**3)
print (obj3.var**5)
print ("This is the end of my code")

