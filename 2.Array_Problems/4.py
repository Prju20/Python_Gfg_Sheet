#Python Program for Reversal algorithm for array rotation
"""
Input: arr[] = [1,2,3,4,5,6,7]
           d = 2
Output: arr[] = [3,4,5,6,7,1,2]
"""
def change(arr,d):
    n= len(arr)
    arr1=arr[0:d]
    arr2=arr[d:n+1]
    array = arr2 + arr1
    return array

arr=[1,2,3,4,5,6,7]
d=2
print(change(arr,d))