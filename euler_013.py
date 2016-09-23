"""
Large sum
Problem 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
import os, numpy as np

infile = open(os.path.join(os.getcwd(), "p_013_in.txt"),"r")

data = [line.rstrip() for line in infile.readlines()]

infile.close()

answer = sum([int(i) for i in data])
print str(answer)[:10]