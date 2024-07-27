#Python Program for How to check if a given number is Fibonocci number?
"""
Input: 8
Output: Yes
`
Input: 34
Output: No

Input: 41
Output: No

A number is Fibonacci if and only if one or both of (5*n*n+4) or (5*n*n-4) is a perfect square
"""
import math

def isPerfectSquare(x):
    s= int(math.sqrt(x))
    return s*s == x

def checkVal(s):
    k=(5*s*s)+4
    p=isPerfectSquare(k)
    if p == True:
        print("yes")
    else:
        print("No")

input=34
print(checkVal(input))
