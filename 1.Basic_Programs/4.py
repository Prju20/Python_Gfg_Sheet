# Python Program for simple interest
P=int(input("Enter Principal Amount: "))
R=int(input("Enter Rate of Interest: "))
T=int(input("Enter Time: "))
SI=(P*R*T)/100
print("The principal amount is {0}, rate of interest is {1} and given time is {2} then simple interest is {3}".format(P,R,T,SI))