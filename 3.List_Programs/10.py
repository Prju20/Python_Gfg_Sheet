#Python Program to find largest number in a list
"""
Input: list1 = [10,20,4]
Output: 20
"""
def largest(list):
    sortedArr=sorted(list)
    return sortedArr[-1]

list1=[10,20,4]
print(largest(list1))