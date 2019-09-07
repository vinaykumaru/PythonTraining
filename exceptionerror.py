import sys
print("Trying some error and exception")

try:
	number = int(input("Enter a number: "))

except ValueError:
	print("ops.. Numbers only")
	sys.exit()

print("you entered ", number)
