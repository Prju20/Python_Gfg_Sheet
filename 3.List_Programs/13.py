#Python Program to print even numbers in a list
"""
Input: list1= [2,7,5,64,14]
Output: [2,64,14]

Input: list2=[12,14,95,3]
Output: [12,14]
"""
def evenList(list):
    even=[]
    for i in list:
        if i%2==0:
            even.extend([i])
    return even

#Input=[2,7,5,64,14]
Input=[12,14,95,3]
print(evenList(Input))