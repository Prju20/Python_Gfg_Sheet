# Python Program for factorial of a number
number = int(input("Enter the number for finding its factorial: "))
fact=1
for i in range(1,number+1,1):
    fact=fact*i

print(f"The factorial of the number is {fact}")