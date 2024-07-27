#Python Program for cube sum of first n natural numbers 
"""
Input: n=5
Output: 225
Explanation: cube(1)+cube(2)+cube(3)+cube(4)+cube(5)

Input: n = 7
Output: 784
Explanation: cube(1)+cube(2)+cube(3)+cube(4)+cube(5)+cube(6)+cube(7) = 784

"""
def cube(val):
    return val*val*val

def sum(value):
    k=0
    for i in range(1,value+1,):
        k+=cube(i)

    return k

s=int(input("Enter the value: "))
print(sum(s))