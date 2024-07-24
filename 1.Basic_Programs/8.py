#Python Program to print all Prime numbers in an interval
n = int(input("Enter the number for finding prime numbers: "))

if n<=1:
    print("The given numbers cannot give prime numbers")
else:
    for i in range(2,n,):
        list=list+i
    print(list)
    # for j in range(2,i,):
    #     if i%j !=0:
    #         print(f"The prime is {i}")         