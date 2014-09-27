import operator

def factoral(x):
	tot=0
	nums=[int(n) for n in str(x)]
	#print "nums",nums
	for n in nums:
		if n != 0:
			sumStr="*".join([str(s) for s in range(1,n+1)])
			#print "sumStr",sumStr, eval(sumStr)
		else:
			sumStr = "1"
		tot += eval(sumStr)
	return tot

print factoral(9)*7
print factoral(145), 145
print factoral(40585), 40585

answer=145

print "starting the calc"

for x in range(146,2540161):
	a=factoral(x)
	if a==x:
		answer += x



"""
for x in range(145,146):
	a=factoral(x)
	if a==x:
		answer += x
"""
	
print "Answer is ", answer
