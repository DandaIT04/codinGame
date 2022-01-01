# codinGame
Solutions for codinGame Clash of Code

# 1_codinGame
The problem statement: Find the amount of occurences of the string in an input e.g find RAGE in rage rAgE rageegege RAGE
After receiving the input, i simply put the input in a list and via text.split(), iterate through it, convert RAGE and elements in list to lowercase, if RAGE in list, count + 1

# 2_codinGame
I actually had fun with this problem. No statements, only inputs and outputs.
Input = 3, uppercase
Output = A B C
Basically, we are to print alphabets according to the amount given and if it is uppercase or lowercase

# 3_codinGame
Asked to check if a number is perfect. A number is perfect as long as it is even

# 4_codinGame
question_prefix = how to
n = number of examples
row = ["how to be good at coding","good at something","how to be software engineer"]
print(row) if row starts with question prefix is my solution

# 5_codinGame
find the exact day in numbers when tom's birthday will fall on. 1 = monday, 2 = tuesday etc
if m+n > 7 means his birthday is next week, so just take m+n - 7 so that it starts on next week.

# 6_codingame
basically print the folder directory path thingy game e.g downloads/pictures/hello.png
num is number of folders the file is in
folder is folder name
filename is filename
extension is the extension name of the file

# 7_codingame
Problem:
Return second highest value in a list
w,x,y,z int numbers e.g 100,103,102,101
Could've just done theList = [w,x,y,z]

# 8_codingame
problem:
input = 15243 input = enaet
output = eaten

Put both inputs into a list. Then first input into dict key and second input into dict value. Sort the dict based on items(). list the dict values into a variable
Lastly, do a for loop to to append list elements into a string variable. Print the string variable.
Did not manage to solve this during the clash but 15mins after clash so took 30minutes overall. Actually a fun problem.

# 9_codingame
problem:
print sum of all even numbers from 0 to given number n.

# 10_codingame
No problem statement. just input and output given and i was supposed to figure out what the problem is.
string 1 input = 0001
string 2 input = 1011
output = 1011

Basically, if value of the index of either one of the two strings contains "1", return "1" else "0" into a new string variable. print result.
