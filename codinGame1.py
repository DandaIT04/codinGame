import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
text = input()

x = text.split()

count = 0
for i,value in enumerate(x):
    if s.lower() in value.lower():
        count = count + 1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(count)
