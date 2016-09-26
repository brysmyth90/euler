"""Power digit sum
Problem 16
2pow15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2pow1000?"""

big_num = 2**1000

big_num_str = str(big_num)

big_num_list = [int(c) for c in big_num_str]

answer = sum(big_num_list)

print answer