#Python | Reversing a List
"""
Input: list=[4,5,6,7,8,9]
Output: [9,8,7,6,5,4]
Explanation: The list we are having in the output is reversed to the list we have in the input.
"""
def reverse(list):
        k=len(list)
        rev=[]
        for i in range(0,k):
            rev.extend([list[-1-i]])
        return rev

list=[4,5,6,7,8,9]
print(reverse(list))
