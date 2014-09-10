
import math

def primeCheck(x):
	top=int(math.sqrt(x))+1
	isPrime=True
	#facTests=[2]+[n for n in range(3,int(x*0.5)+1)]
	facTests=[n for n in range(2,int(x*0.5)+1)]
	#print x,"facTests",facTests
	for fac in facTests:
		#print "will test if %d modo %d is zero"%(x,fac)
		if x%fac==0:
			return False
	return True
	
def factors(x):
	facs=[n for n in range(2,int(x*0.5)+1) if x%n==0 and primeCheck(n)]
	return facs
	
for x in range(0,100):
	print x,factors(x)
