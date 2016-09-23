"""
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?
"""
import os, numpy as np

infile = open(os.path.join(os.getcwd(), "p_011_in.txt"),"r")

data = [line.rstrip().split(" ") for line in infile.readlines()]

infile.close()

for x in range(len(data)):
    for y in range(len(data[x])):
        data[y][x] = int(data[y][x])

arr=np.array(data)
data=np.swapaxes(arr,0,1)


off = [ [[0,0],[1,0],[2,0],[3,0]], [[0,0],[0,1],[0,2],[0,3]], [[0,0],[1,1],[2,2],[3,3]], [[0,0],[-1,-1],[-2,-2],[-3,-3]],
        [[0,0],[-1,1],[-2,2],[-3,3]], [[0,0],[1,-1],[2,-2],[3,-3]] ]

store = set()

for x in range(0,20):
    for y in range(0,20):
        for o in off:
            print x,y,o
            try:
                tot = (data[x+o[0][0]][y+o[0][1]] * data[x+o[1][0]][y+o[1][1]] * data[x+o[2][0]][y+o[2][1]] * data[x+o[3][0]][y+o[3][1]])
                print x,y, (data[x+o[0][0]][y+o[0][1]] , data[x+o[1][0]][y+o[1][1]] , data[x+o[2][0]][y+o[2][1]] , data[x+o[3][0]][y+o[3][1]])
                store.add (tot)
            except IndexError:
                print "bust", x,y
   
            
            
print max(store)