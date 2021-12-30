import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# question is if a number is perfect. A number is perfect as long as it is even.

if n % 2 != 0:
    print("not perfect")
else:
    print("perfect")    
