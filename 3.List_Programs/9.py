#Python Program to find smallest number in a list
"""
Input: list1=[10,20,4]
Output: 4

Input: list2=[20,10,20,1,100]
Output: 1
"""
def smallest(list):
    sortedList=sorted(list)
    return sortedList[0]

#list1=[10,20,4]
list2=[20,10,20,1,100]
print(smallest(list2))