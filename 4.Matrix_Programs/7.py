#Python | Get Kth Column of Matrix
"""
Input:[[4,5,6],[8,1,10],[7,12,5]] k=2
Output:[6,10,5]
"""
def findPosition(mat,k):
    length=len(mat)
    width=len(mat[0])
    pos=[0,0,0]
    for i in range(0,length):
        for j in range(k+1):
            pos[i]=mat[i][j]
    return pos
mat=[[4,5,6],[8,1,10],[7,12,5]]
print(findPosition(mat,2))

            

