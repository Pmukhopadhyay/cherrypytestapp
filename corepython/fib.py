def fib(limit):
    first = 0
    last = 1
    temp = first
    print first
    while last <= limit :
        first = temp
        print last
        temp = last
        last =  first + last
fib(5)
print '========================================================'
def fibByRec(limit):
	num = 0
	if limit - 2 >= 0 and limit -1 >= 0:
		num = fibByRec(limit -1) + fibByRec(limit - 2)
	elif limit - 2 >= 0 and limit -1 <=0:
		num = fibByRec(limit -1) + 1
	else:
		num = 1
	return num
print 0
for i in range(0,5,1):
	print fibByRec(i)

