from twisted.internet import reactor,defer

class Custom:
	def methodA(self, a):
		d = self.d
		self.d = None
		if a % 2 == 0:
			d.callback(a*4)
		else:
			d.errback(ValueError("error .. a is odd.."))

	def methodB(self, r):
		return ">>>%s" % r

	def methodC(self, a):
		self.d = defer.Deferred()
		reactor.callLater(1, self.methodA, a)
		self.d.addCallback(self.methodB)
		return self.d

def printResult(cc):
	print cc

def printError(errorMessage):
	import sys
	sys.stderr.write (str(errorMessage))


obj = Custom()
obj1 = obj.methodC(4)
obj1.addCallback(printResult)
obj1.addErrback(printError)

'''
obj = Custom()
obj1 = obj.methodC(7)
obj1.addCallback(printResult)
obj1.addErrback(printError)
'''
reactor.callLater(4, reactor.stop)
reactor.run()
