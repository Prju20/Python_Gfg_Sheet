#Python Program to interchange first and last elements in a list 
"""
Input:[12,35,9,56,24]
Output:[24,35,9,56,12]

Input:[1,2,3]
Output:[3,2,1]
"""

def swap(input):
    temp=input[0]
    input[0]=input[-1]
    input[-1]=temp
    return input

arr= [12,35,9,56,24]
print(swap(arr))


    