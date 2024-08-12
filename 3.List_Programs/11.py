#Python Program to find second largest number in a list
"""
Input: list1=[10,20,4]
Output: 10

Input: list2=[70,11,20,4,100]
Output:70
"""
def second_largest(list):
    sortedList=sorted(list)
    return sortedList[-2]

list=[70,11,20,4,100]
print(second_largest(list))