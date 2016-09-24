"""Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n ? n/2 (n is even)
n ? 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import sys
sys.setrecursionlimit(10000)

def make_chain(i):
    if i[-1]==1:
        return i
    else:
        if i[-1]%2==0:
            i.append(i[-1]/2)
            return make_chain(i)
        else:
            i.append(i[-1]*3+1)
            return make_chain(i)
    

chain = {}


#chain[13] = make_chain([13])

for x in range(1,1000000):
    chain[x] = make_chain([x])

longest = 0
answer = 0

for k in chain:
    this_length = len(chain[k])
    if this_length > longest:
        longest = this_length
        answer = k
        
print answer