import operator

def factoral(x):
	tot=0
	nums=[int(n) for n in str(x) if n!="0"]
	#print "nums",nums
	for n in nums:
		sumStr="*".join([str(s) for s in range(1,n+1)])
		#print "sumStr",sumStr
		tot += eval(sumStr)
	return tot

print factoral(9)*7
print factoral(40585)

answer=145
for x in range(146,2540161):
	a=factoral(x)
	if a==x:
		answer += x
		
print "Answer is ", answer
