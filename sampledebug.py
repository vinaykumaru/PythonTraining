import pdb
def perform(a,b):
	x=a+b*b**2	
	return x
var = 100
var1 = 200
pdb.set_trace()
ans = perform(var,var1)
print (ans)


''' 
n => next execute
c => complete execuation
l => list 3 lines before and after current line
s => step into the function
cl => clear all break points
b[int] => set break points at line number ex. b10
b[func] => break at function name ex. bperform
cl => clear all break points
cl[int] => clear breakpoint at line number ex. cl10
p => print
'''


