#Python Program to print negative numbers in a list
"""
Input: list1=[12,-7,5,64,-14]
Output: -7,-14

Input: list2 = [12,14,-95,3]
Output: -95
"""
def negative(list):
    minus=[]
    for i in list:
        if i < 0:
            minus.extend([i])
    return minus

list=[12,-7,5,64,-14]
print(negative(list))