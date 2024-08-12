#Python Program to check if given array is Monotonic
"""
Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, A[i] <= A[j]. 

An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. 

Return Type: Boolean value, “True” if the given array A is monotonic else return “False” (without quotes).

Examples: Input: 6 5 4 4
          Output: true

          Input: 5 15 20 10
          Output: false

"""

"""
def Increasing(arr):
    sortedArr=sorted(arr)
    return arr==sortedArr

def Decreasing(arr):
    sortedArr=sorted(arr)
    length=len(sortedArr)
    reverse=[]
    for i in range(0,length):
        reverse.extend([sortedArr[-1-i]])
    return reverse==arr

def Monotonic(arr):
    if Increasing(arr)==True:
        return True
    elif Decreasing(arr)==True:
        return True
    else:
        return False



        
        

arr=[6,5, 4, 4]
print(Monotonic(arr))

"""

def Increasing(arr):
    return arr == sorted(arr)

def Decreasing(arr):
    return arr == sorted(arr, reverse=True)

def Monotonic(arr):
    return Increasing(arr) or Decreasing(arr)

arr = [5,15,20,10]
print(Monotonic(arr))
