import time
"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_pal(x):
    if (str(x)==str(x)[::-1]):
        return True
    else:
        return False


start = time.time()
largest = 0

for x in range(100,1000):
    for y in range(100,1000):
        this_num = x*y
        if is_pal(this_num) and this_num > largest:
            #print this_num, largest
            largest = this_num
            
print largest, time.time()-start