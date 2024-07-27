#Python Program for nth Fibonocci number
"""
F(n)=f(n-1)+f(n-2)
series: 01 1 2 3 5 8 13
"""
n=int(input("Enter n: "))
f0=0
f1=1
print(f0)
print(f1)
for i in range(2,n+1,):
    f=f0+f1
    f0=f1
    f1=f
    print(f)

    


