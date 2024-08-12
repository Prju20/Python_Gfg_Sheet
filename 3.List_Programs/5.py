#Different ways to clear a list in Python
"""
Input: [2,3 ,5, 6,7]
Output:[]
Explanation: Python list is cleared and it becomes empty so we have returned empty list.
"""
def empty(arr):
    length=len(arr)
    for i in arr:
        del(arr[0:length+1])
    return arr

arr=[2,3,5,6,7]
print(empty(arr))