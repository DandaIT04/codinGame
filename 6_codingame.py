import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# basically print the folder directory path thingy game e.g downloads/pictures/hello.png
# num is number of folders the file is in
# folder is folder name
# filename is filename
# extension is the extension name of the file

num = int(input())

theAnswer = ""

for i in range(num):
    folder = input()
    theAnswer = theAnswer + folder + "/"

filename = input()
extension = input()

theAnswer = theAnswer + filename
theAnswer = theAnswer + "." + extension
print(theAnswer)    
