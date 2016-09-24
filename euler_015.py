
min_int = 1048576
max_int = 1099510579200
length = 40
bal=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
     '1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']


#min_int = 4
#max_int = 16
#length = 4
#bal=['0','0','1','1']

answer = 0

x = min_int
while x <= max_int:
    s= list(str(bin(x))[2:].zfill(length))
    s.sort()
    if s == bal:
        answer += 1
        #print x,list(str(bin(x))[2:].zfill(4)),s
        print x/1099510579200.0
    x += 1
        
print answer
    
