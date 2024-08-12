#Python Program to print all positive numbers in a range
"""
Input: start=-4,end=5
Output:0,1,2,3,4,5

Input:start =-3,end=4
Output:0,1,2,3,4
#use no list
"""

def interval(start,end):
    for i in range(start,end+1):
        if i >=0:
            print(i)

#print(interval(-4,5))
print(interval(-3,4))