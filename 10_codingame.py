import sys
import math

n_1, n_2 = input().split()

n_3 = ""

for i in range(len(n_1)):
    if n_1[i] == "1" or n_2[i] == "1":
        n_3 += "1"
    else:
        n_3 += "0"

print(n_3)  
