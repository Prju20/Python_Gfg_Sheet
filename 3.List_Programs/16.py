#Python Program to print all odd numbers in a range
"""
Input: start=4,end=15
Output:5,7,9,11,13,15

Input: start = 3,end=11
Output:3,5,7,9,11
#use no list
"""
def oddInterval(start,end):
    for i in range(start,end+1):
        if i%2 !=0:
            print(i)

print(oddInterval(4,15))