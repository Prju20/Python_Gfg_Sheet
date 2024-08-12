#Python | Matrix creation of n*n
"""
#use list comprehension
Input: 4
Output:[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
"""
def creation(n):
    count=0
    mat=[]
    for i in range(0,n):
        for j in range(0,n):
            mat[i][j]=mat.extend([count+1+i])
    return mat

print(creation(4))