import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# So this problem is amazing. No statements are given, only input and output.
# Basically, the input is something like "3 UPPER"
# output is "A B C"
# And after looking at the rest of the output, i can conclude that they want us to print
# print out ABC alphabets according to the length and if it is uppercase or lowercase

case_or_trick = input()
n = int(input())
case_or_trick = case_or_trick.lower()

if n == 0 or n > 26:
    print("ERROR")
else:
    a = "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    a = a.split()

    theAnswer = []
    for i in range(n):
        if "lower" in case_or_trick:
            theAnswer.append(a[i].lower())
        else:
            theAnswer.append(a[i].upper())  

    toPrint = ""
    rangeOfAnswer = len(theAnswer)
    for j in range(rangeOfAnswer):
        if j == len(theAnswer) - 1:
            toPrint = toPrint + theAnswer[j]
        else:    
            toPrint = toPrint + theAnswer[j] + " "  

    print(toPrint)       
