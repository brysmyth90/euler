"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
 
What is the 10 001st prime number?
"""
 
import math
 
def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        #print x,i
        if x%i==0:
            return False
    return True
 
x=1
 
primes = set()
 
while len(primes) < 10001:
    x += 1
    if is_prime(x):
        primes.add(x)
     
 
print x