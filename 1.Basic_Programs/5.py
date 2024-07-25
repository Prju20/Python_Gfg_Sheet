# Python Program for compound interest 
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter time : "))
amount=round(p*((1+r/100)**t),1)
CI=amount - p
print(f"The compound interest is {CI}")