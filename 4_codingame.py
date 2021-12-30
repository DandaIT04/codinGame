import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# question_prefix = how to
# n = number of examples
# row = ["how to be good at coding","good at something","how to be software engineer"]
# print(row) if row starts with question prefix is my solution

question_prefix = input()
n = int(input())

notFound = 0

for i in range(n):
    row = input()
    if row.startswith(question_prefix):
        print(row)
    else:
        notFound += 1

if notFound == n:
    print("EMPTY")            
