import sys
import math

# Find the sum of the first n odd integers!
# (e.g. n=4: 1+3+5+7=16)

n = int(input())  # the number of odd integers

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

"""
count = 1
theSum = 0

while n!= 0:
    n = n - 1
    theSum = theSum + count
    count = count + 2

print(theSum)
"""

print(n*n)
