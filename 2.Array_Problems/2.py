#Python Program to find largest element in an array
"""
Input: arr[]={10,20,4}
Output: 20
Input: arr[]={20,10,20,4,100}
Output:100
"""
def largest(arr):
    sortedArr=sorted(arr)
    return sortedArr[-1]

#arr=[10,20, 4]
arr=[20,10,20,4,100]
print(largest(arr))
