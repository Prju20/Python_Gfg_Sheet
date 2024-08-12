#Python Program to check whether the string is Symmetrical or Palindrome
"""
Input: khokho
Output:
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output: 
The entered string is symmetrical
The entered string is palindrome
"""
def symmetrical(string):
    length=len(string)
    k= length // 2
    str=string[0:k]
    str1=string[k:length]
    if str==str1:
        return "This is symmetrical"
    else:
        return "This is not symmetrical"

def palindrome(string):
    length=len(string)
    str=""
    for i in range(0,length):
        str=str+string[-1+i]
    if string==str:
        return "This is plaindrome"
    else:
        return "This is not plaindrome" 



string="khokho"
#string="catmat"
print(symmetrical(string))
print(palindrome(string))
