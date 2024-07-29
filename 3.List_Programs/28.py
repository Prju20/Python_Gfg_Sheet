#Python | Sum of number digits in List
"""
Input:list=[12,67,98,34]
Output: [3,13,17,7]
"""

def Sum(list):
    sum=0
    for i in list:
        sum=sum+i

    return sum

L=[1,2,3,4,5]
print(Sum(L))
