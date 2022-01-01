import sys
import math

n = int(input())

theValue = 0

for i in range(n+1):
    if i % 2 == 0:
        theValue += i

print(theValue)            
