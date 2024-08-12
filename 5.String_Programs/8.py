#Find length of a string in python (4 ways)
"""
Input: 'abc'
Output: 3

Input: 'hello world'
Output: 13

Input:' h e l  l o '
Output: 12

Methods#1:
Using the built-in function len. The built-in function len returns the number of items in a container

Method#2:
Using for loop and in operator. A string can be iterated over, directly in a for loop. Maintaining a count of the number of iterations will result in the length of the string

Method#3:
Using while loop and Slicing. We slice a string making it shorter by 1 at each iteration will eventually result in an empty string. This is when while loop stops. Maintaining a count of the number of iterations will result in the length of the string.
"""

def length(string):
    count=0
    for i in string:
        count+=1
    return count

string=' h e l  l o '
print(length(string))
