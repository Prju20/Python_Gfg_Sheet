#Python Program for array rotation 
"""
nput arr[] = [1, 2, 3, 4, 5, 6, 7, 8], d = 1, size = 8

1) Reverse the entire list by swapping first and last numbers

   i.e start=0, end=size-1

2) Partition the first subarray and reverse the first subarray, by swapping first and last numbers.

   i.e start=0, end=size-d-1

3) Partition the second subarray and reverse the second subarray, by swapping first and last numbers.

   i.e start=size-d, end=size-1

i.e: 1 2 3 4 5 6 7 8(Reverse the array)
     8 7 6 5 4 3 2 [1-Sub array 2,size=d]
    (Sub array 1)
    (size= length of array - d)

     2 3 4 5 6 7 8 1(Reverse both sub arrays)
     
"""