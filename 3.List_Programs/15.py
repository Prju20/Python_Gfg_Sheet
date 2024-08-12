#Python Program to print all even numbers in a range
"""
Input: start =4, end =15
Output: 4,6,8,10,12,14

Input:start = 8,end=11
Output:8,10
#use no list
"""
def evenInterval(start,end):
    for i in range(start,end):
        if i%2==0:
            print(i)

start=4
end=15
print(evenInterval(start,end))