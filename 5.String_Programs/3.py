#Reverse words in a given String in Python
"""
Input: str="geeks quiz practice code
Output: str=code practice quiz geeks

Input: str="my name is laxmi
Output: str= laxmi is name my
"""
def different(string):
    string=string.split()
    length=len(string)
    str=" "
    for i in range(0,length):
        str=str+string[-1-i]+" "
        
    return str
str="geeks quiz practice code"
print(different(str))