import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

m = int(input())
n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# find the exact day in numbers when tom's birthday will fall on. 1 = monday, 2 = tuesday etc
# if m+n > 7 means his birthday is next week, so just take m+n - 7 so that it starts on next week.

if m+n > 7:
    print((m+n) - 7)
else:
    print(m+n)    
