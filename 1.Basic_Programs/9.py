#Python Program to check whether a number is Prime or not 
"""
Input: n=11
Output: True

Input: n=1
Output: False

Explanation: A prime number is a natural number greater than 1 that
 has no positive divisors other than 1 and itself.
  The first few prime numbers are {2, 3, 5, 7, 11, ….}. 
"""

def prime(n):
    if n == 0 or n==1:
        return False
    else:
        for i in range(2,n,):
            k=n%i
            if k==0:
                return False
                break

    return True

n=1
print(f"The given number {n} is {prime(n)}")



