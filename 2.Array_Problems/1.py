#Python Program to find sum of array 
"""
Input: arr[]={1,2,3}
Output: 6
Explanation: 1 + 2 + 3 = 6
"""

def sum(arr):
    sum=0
    for i in arr:
        sum=sum+i

    return sum

arr= [12,3,4,15]
ans=sum(arr)
print(f"The sum of the given {arr} is {ans}")
