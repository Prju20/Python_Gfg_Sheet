#Python Program to print all negative numbers in a range
"""
Input: a=-4, b=5
Output: -4,-3,-2,-1

Input: a=-3, b=4
Output: -3,-2,-1
#use no list
"""
def negative(start,end):
    for i in range(start,end):
        if i<0:
            print(i)

print(negative(-4,5))