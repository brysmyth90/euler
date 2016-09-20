import math
"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

bignum=600851475143

def is_prime(x):
    for i in range(2,int(math.sqrt(x))+1):
        #print x,i
        if x%i==0:
            return False
    return True

def is_factor(x,y):
    if y%x==0:
        return True
    else:
        return False

for n in range(1,int(math.sqrt(bignum))):
    if is_factor( (int(math.sqrt(bignum)))-n,bignum ) and is_prime(int(math.sqrt(bignum)-n)):
        print int(math.sqrt(bignum)-n)
        break
        
        
        
