fib=[1,2]
while fib[-1]<=4000000:
	fib.append(sum(fib[-2:-1]))
print "Answer is %d"%sum([n for n in fib if n%2==0])
