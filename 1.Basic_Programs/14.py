#Python Program for Sum of squares of first n natural numbers 
"""
Input : N=4
Output : 30
Explanation : square(1)+square(2)square(3)+square(4)
             = 1 + 4 + 9 + 16
             = 30
"""
def Square(int):
    return int*int

def Sum(value):
    n=0
    for i in range(1,value+1,):
        n += Square(i)

    return n
    

a=int(input("Enter the value of a: "))
print(f"The sum of the square of {a} is {Sum(a)}")
