#Python Program to print odd numbers in a list
"""
Input: list1=[2,7,5,64,14]
Output:[7,5]

Input: list2=[12,14,95,3,73]
Output:[95,3,73]
"""
def oddList(list):
    odd=[]
    for i in list:
        if i%2 !=0:
            odd.extend([i])
    return odd

list1=[2,7,5,64,14]
list2=[12,14,95,3,73]
print(oddList(list2))