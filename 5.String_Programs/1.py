#Python Program to check if a string is palindrome or not
"""
Input: malayalam
Output: Yes
Input: geeks
Output: No
"""
def palindrome(string):
    length=len(string)
    k=""
    for i in range(0,length):
        k=k+string[-1-i]
    return string==k

#string="malayalam"
string="geeks"
print(palindrome(string))
