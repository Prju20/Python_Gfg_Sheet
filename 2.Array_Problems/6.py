#Python Program for Find reminder of array multiplication divided by n
"""
Input:arr[]={100, 10 , 5,25,35,14},
       n=11
Output: 9
Explanation : 100 x 10 x 5 x 25 x 35 x 14 = 61250000 %11 =9

Input: arr[]={100,10},
        n=5
Output: 0
Explanation: 100 x 10 = 1000 % 5 =0
"""

def multiply(arr,n):
    multiply=1
    for i in arr:
        multiply=multiply * i
    ans=multiply % n
    return ans

# arr=[100,10,5,25,35,14]
# n=11
arr=[100,10]
n=5

print(f"The value of the multiply of arr is {arr} divided by {n} have remainder {multiply(arr,n)}")


    