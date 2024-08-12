#Python | Multiply all numbers in the list
"""
Input: list1=[1,2,3]
Output: 6
Explanation: 1*2*3=6

Input: list1=[3,2,4]
Output: 24
"""
def multiply(arr):
    multiply=1
    for i in arr:
        multiply*=i
    return multiply
list=[1,2,3]
print(multiply(list))