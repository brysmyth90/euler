"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Answer:
	6857
"""


import math

def primeCheck(x):
	top=int(math.sqrt(x))+1
	isPrime=True
	facTests=[2]+[n for n in xrange(3,top,2)]
	print "facTests",facTests
	for fac in facTests:
		if x%fac==0:
			return False
	return True	


big=600851475143
#big=13195
top=int(math.sqrt(big))+1
print "top is %d"%top
facs = [2]+[n for n in range(3,top,2) if big%n==0]
print "facs",facs
answer=False
while (not answer and facs):
	test = facs.pop()
	print "testing if %d is prime..."%test
	if primeCheck(test):
		answer=test

#print "facs",facs
print "answer = %d"%answer
