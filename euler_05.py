"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def div_all(x):
    nums = [20,19,18,17,16,15,14,13,12,11]
    #nums = [10,9,8,7,6]
    for i in nums:
        if x%i != 0:
            return False
    return True

solved = False
x=0

while not solved:
    x += 2
    solved = div_all(x)
    
    
print x