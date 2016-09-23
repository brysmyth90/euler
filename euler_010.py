"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        #print x,i
        if x%i==0:
            return False
    return True

print sum([i for i in range(2,2000000) if is_prime(i)])
