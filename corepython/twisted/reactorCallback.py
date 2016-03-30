from twisted.internet import defer,reactor

def myFunction(x):
	d = defer.Deferred()
	reactor.callLater(2,d.callback,x*3)
	return d

def printResult(x):
	print 'from printResult',x

d = myFunction(5)
d.addCallback(printResult)
reactor.callLater(2,reactor.stop)
reactor.run()



