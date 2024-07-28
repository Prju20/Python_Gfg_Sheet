#Python Program to split the array and add the first part to the end
"""
There is a given array and split it from a specified position, and move the first part of the array add to the end.
Input: arr[] = {12, 10, 5, 6, 52, 36}
        k=2
Output: arr[] = {5, 6, 52, 36, 12, 10}
Explanation : Split from index 2 and first part {12,10} add to the end .

Input: arr[]: {3,1,2}
        k =2
        Output: arr[]={1,2,3}
        Explanation : Split from index 1 and first add to the end.
"""

def split(arr,k):
    n=len(arr)
    arr1=arr[0:k]
#     print(arr1)
    arr2=arr[k:n+1]
#     print(arr2)
    array=arr2+arr1
    return array

# arr = [12, 10, 5, 6, 52, 36]
# k=2
arr=[3,1,2]
k =2
print(split(arr,k))
#print(f"The given is }")