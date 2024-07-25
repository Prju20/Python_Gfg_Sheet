# Python Program to check Armstrong Number
value=int(input("Enter the number: "))
order=len(str(value))
number=value
no=0
while number!=0:
    digit=number%10
    value=number//10
    armstrong=no+pow(digit,order)
    no=armstrong

print(armstrong)
print(type(value))
print(value)
if value==armstrong:
    print(True)
else:
    print(False)
