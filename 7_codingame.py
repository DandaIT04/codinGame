import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

########################################################
"""
Problem:
Return second highest value in a list
w,x,y,z int numbers e.g 100,103,102,101

Could've just done theList = [w,x,y,z]
"""
########################################################

n = int(input())

for i in range(n):
    w, x, y, z = [int(j) for j in input().split()]
    theList = []
    theList.append(w)
    theList.append(x)
    theList.append(y)
    theList.append(z)
    theList.sort()
    print(theList[2])
    theList = []
