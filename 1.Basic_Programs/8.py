#Python Program to print all Prime numbers in an interval
""" TO find all the numbers from given starting point to ending point
i.e 2,3,5,7,11,..
"""
def isprime(param):
    for i in range(2,param,):
        k=param%i
        if k==0:
            return None
            break
    return param
         

def interval(n):
    for i in range(2,n+1,):
        s= isprime(i)
        if s == None:
            pass
        else:
            print(s)
        


n = int(input("Enter the number for finding prime numbers: "))
print(interval(n))
