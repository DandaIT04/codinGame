import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# find if string s exists in text. e.g Rage in text = RAGE rage rAge RAGEEEE

s = input()
text = input()

x = text.split()

print(s)
print(x)

count = 0
for i,value in enumerate(x):
    if value in s:
        count = count + 1
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(count)