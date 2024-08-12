#Python Program to print even length words in a string
"""
Input: s="This is a python language"
Output: This is python language

Input: s = "i am laxmi"
Output: am
"""
def even_length(string):
    string=string.split()
    new=""
    for i in string:
        even=len(i)
        if even%2==0:
            new=new+i+" "
    return new

#s="This is a python language"
s = "i am laxmi"
print(even_length(s))

            