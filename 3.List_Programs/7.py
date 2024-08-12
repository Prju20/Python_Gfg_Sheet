#Python Program to find sum of elements in list 
"""
Input: [12,15,3,10]
Output: 40

Input: [17,5,3,5]
Output: 30
"""

def sum(list):
    sum=0
    for i in list:
        sum=sum+i

    return sum

list=[12,15,3,10]
print(sum(list))