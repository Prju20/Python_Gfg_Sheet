# Python Program to check Armstrong Number
"""def findarmstrong(order,value):
    no=0
    while value!=0:
        digit=value%10
        value=value//10
        no+=pow(digit,order)
    
    return no
def checkarmstrong(value):
    if findarmstrong != value:
        return True
    else:
        return False
    


value=int(input("Enter the number: "))
order=len(str(value))
print(findarmstrong(order,value))
print(checkarmstrong(value))"""
# Python Program to check Armstrong Number
def findarmstrong(order, value):
    no = 0
    while value != 0:
        digit = value % 10
        value = value // 10
        no += pow(digit, order)
    
    return no

def checkarmstrong(value):
    order = len(str(value))
    return findarmstrong(order, value) == value

value = int(input("Enter the number: "))
order = len(str(value))
print("Computed sum:", findarmstrong(order, value))
if checkarmstrong(value):
    print(f"{value} is an Armstrong number.")
else:
    print(f"{value} is not an Armstrong number.")
#nothing changed
