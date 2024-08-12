#Python Program to find N largest elements from a list
"""
Input: [4,5,1,2,9]
        N=2
Output: [9,5]

Input: [81,52,45,10,3,2,96]
        N=3
Output:[96,81,52]
"""
def largesublist(list,n):
    sortedList=sorted(list)
    length=len(sortedList)
    reverse=[]
    for i in range(0,length):
        reverse.extend([sortedList[-1-i]])
    li=reverse[0:n]
    return li

#list=[4,5,1,2,9] N=2
list=[81,52,45,10,3,2,96]
#N=3
print(largesublist(list,3))