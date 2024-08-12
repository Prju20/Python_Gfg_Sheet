#Adding and Substracting Matrices in Python
"""
Suppose we have two matrices A and B.
A=[[1,2],[3,4]]
B=[[4,5],[6,7]]

then we get 
A+B = [[5,7],[9,11]]
A-B=[[-3,-3],[-3,-3]]

"""
def Addition(mat1,mat2):
    length=len(mat1)
    width=len(mat1[0])
    Add=[[0,0],[0,0]]
    for i in range(0,length):
        for j in range(0,width):
            Add[i][j]=mat1[i][j]+mat2[i][j]
    return Add

def Subtraction(mat1,mat2):
    length=len(mat1)
    width=len(mat1[0])
    Minus=[[0,0],[0,0]]
    for i in range(0,length):
        for j in range(0,width):
            Minus[i][j]=mat1[i][j]-mat2[i][j]
    return Minus



A=[[1,2],[3,4]]
B=[[4,5],[6,7]]
print(Addition(A,B))
print(Subtraction(A,B))