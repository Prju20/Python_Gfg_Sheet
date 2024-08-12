#Python Program to add two Matrices
"""
x=[[1,2,3],
   [4,5,6],
   [7,8,9]]

Y=[[9,8,7],
   [6,5,4],
   [3,2,1]]

Output: 
    result=[[10,10,10],
            [10,10,10],
            [10,10,10]]
"""

def Matrix(mat1,mat2):
   length=len(mat1)
   width=len(mat1[0])
   solution=[[0,0,0],[0,0,0],[0,0,0]]
   for i in range(0,length):
      for j in range(0,width):
         solution[i][j]=mat1[i][j]+mat2[i][j]  
   return solution

X=[[1,2,3],[4,5,6],[7,8,9]]
Y=[[9,8,7],[6,5,4],[3,2,1]]
print(Matrix(X,Y))
    