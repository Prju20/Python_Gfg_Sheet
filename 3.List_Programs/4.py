#Python | Ways to check if elements exists in list
"""
Input: test_list =[1,6,3,5,3,4]
       k=3 #Check if 3 exist or not.
Output: True
Explanation: The output is True because the element we are looking is exist in the list.
use find()method
"""
def find(list,k):
    for i in list:
        if i==k:
            return True
            break
        
    return False

list=[1,3,6,5,4]
print(find(list,3))