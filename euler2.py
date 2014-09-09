"""By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Answer:
	4613732"""
tot=2
fib=[1,2]
while fib[-1]<=4000000:
	#fib.append(sum(fib[-2:-1]))
	fib=[fib[-1]]+[sum(fib)]
	if fib[-1]%2==0:
		tot+=fib[-1]
print "Answer is %d"%tot
