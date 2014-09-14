
import math
import itertools
import operator

"""
test=[2,4,6]
i=itertools.combinations_with_replacement(test,2)
for e in i:
	print e
"""

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
	
def facsMakesNum(x,numsFacs):
	#x is the number, numsFacs is a list of it's prime factors
	numsFacs+=numsFacs #add to itself, a duff way to make two of 'em possible in combinations
	print "facsMakeNum function ", x, numsFacs
	results=[]
	for l in range(3,len(numsFacs)): #to get every possible combination of len 4 and up
		i=itertools.combinations_with_replacement(numsFacs,l)
		for r in i:
			if len(set(r))==3: #test with 3, must be 4 for final answer
				mul=reduce(operator.mul, r, 1) #this multiplies the list so can see if is x
				print "r is ",r, "for ", mul
				results.append(mul)
	if x in results:
		return True
	else:
		return False
	
	
nums=[641,642,643] #this will be the 4 consequitive numbers

for x in range(0,10): #need to replace this with a while loop
	print "nums", nums
	numsFacs=[factors(nums[0]),factors(nums[1]),factors(nums[2])]# get all the prime factors
	if (len(numsFacs[0])>=3 and len(numsFacs[1])>=3 and len(numsFacs[2])>=3): #will need 4 for proper
		print nums, "worth checking"
		#will have the answer when these all return true
		if (facsMakesNum(nums[0],numsFacs[0]) and facsMakesNum(nums[1],numsFacs[1]) and facsMakesNum(nums[2],numsFacs[2])):
			print "WINNER is %d!!! - "%nums[0],nums
			break
		
	nums=[nums[0]+1,nums[1]+1,nums[2]+1]#if wasn't a win then up the numbers in the list
