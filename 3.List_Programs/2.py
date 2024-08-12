#Python Program to swap two elements in a list
"""
Input:List=[23,65,19,90],pos1=1,pos2=3
Output:[19,65,23,90]

Input: List=[1,2,3,4,5],pos1=2,pos2=5
Output:[1,5,3,4,2]

"""
def swap(arr,pos1,pos2):
    temp=arr[pos1-1]
    arr[pos1-1]=arr[pos2-1]
    arr[pos2-1]=temp
    return arr
# List=[23,65,19,90]
list=[1,2,3,4,5]
print(swap(list,2,5))