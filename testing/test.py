def cube(x): return x*x*x

print map(cube,range(2,4))

def fib(n):# write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a,b=0,1
	while a<n:
		print a
		a,b=b,a+b
fib(20)


class Test:
	firstName=None
	lastName=None
	age=0
	
	def __call__(self):
		print "from call method of Test"

	def __init__(self,firstName,lastName,age):
		self.firstName=firstName
		self.lastName=lastName
		self.age=age
	
	@classmethod
	def getFirstName(cls,input):
		a = input.split('|')
		return a[0]

	@staticmethod
	def getAgeFromInput(input):
		a=input.split('|')
		return a[2]

print "age = ",Test.getAgeFromInput('AAAA|BBBB|24')
t=Test("Ram","Singh",24)
print t.getFirstName('AAAA|BBB')
#Test()