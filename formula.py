def my_circle(r):
	return 3.14*r*r

def my_square(s):
	return s**2

def my_rectangle(b,h):
	return b*h/2

choice = int(input("enter \n 1. Area of circle \n 2. Area of square \n 3. Area of rectancle \n 0. To Exit"))

if choice==1:
	var = eval(input("what is r? "))
	print("Area of circle is: ", my_circle(var))
elif choice==2:
	var1 = eval(input("what is s? "))
	print("Area of square is: ", my_square(var1))
elif choice==3:
	var2 = eval(input("what is b? "))
	var3 = eval(input("what is h? "))
	print("Area of rectangle is: ", my_rectangle(var2,var3))
elif choice==0:
	exit()
else:
	print("We need a break")

