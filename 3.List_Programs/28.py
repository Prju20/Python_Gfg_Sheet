#Python | Sum of number digits in List
def Sum(list):
    sum=0
    for i in list:
        sum=sum+i

    return sum

L=[1,2,3,4,5]
print(Sum(L))
