from twisted.internet import defer

def fib(limit):
    first = 0
    last = 1
    temp = first
    d = defer.Deferred()
    while last <= limit :
        first = temp
        temp = last
        last =  first + last

    #print 'from fib>>>',last
    d.callback(last)
    return d

import time

timeBefore = time.time()
d = fib(5)
timeAfter = time.time()
print 'Total time taken to calculate fib no =',(timeAfter - timeBefore)

def printFibNumberReturnedAfterCalc(result):
	print 'The calculated value=',result

d.addCallback(printFibNumberReturnedAfterCalc)

