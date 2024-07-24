#Python Program to check whether a number is Prime or not 
def prime(n):
    for i in range(2,n,):
        prime=(n%i==0)