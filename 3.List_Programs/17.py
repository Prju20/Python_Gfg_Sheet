#Python Program to print positive numbers in a list
"""
Input: list1 = [12,-7,5,64,-14]
Output:12,5,64

Input: list2 = [12,14,-95,3]
Output: [12,14,3]
"""
def positive(list):
    plus=[]
    for i in list:
        if i > 0:
            plus.extend([i])
    return plus
#list=[12,-7,5,64,-14]
list=[12,14,-95,3]
print(positive(list))