import math

a = str(243)
a = list(a)

b = list(a)
b.reverse()

if a == b:
    print("wins")
else:
    print("lose")
