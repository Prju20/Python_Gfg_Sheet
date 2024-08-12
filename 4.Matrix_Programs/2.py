#Python Program to multiply two matrices
"""
Input: X=[[1,7,3],
         [3,5,6],
         [6,8,9]]
       Y=[[1,1,1,2],
         [6,7,3,0]
         [4,5,9,1]]

Output: [[55,65,49,5],
        [57,68,72,12],
        [90,107,111,21]]
"""
def columns(mat1,mat2):
    length=len(mat1[0])
    lenth=len(mat2[0])
    if lenth > length:
      value=lenth
    else:
       value=length
    return value
    
def multiply(mat1,mat2):
   lenth=len(mat1)
   count=1
   mat=[]
   cat=[]
   value=columns(mat1,mat2)
   val= value-lenth
   for i in range(0,lenth+val):
      for j in range(0,value):
        cat.extend([count])
        break
      mat.append(cat)
   return mat

def mult(mat1,mat2):
   val=len(mat1[0])-len(mat2)
   mat=multiply(mat1,mat2)
   for i in range(0,len(mat1)+val):
      for j in range(0,):
        
        break
      mat.append(cat)
      
      
      

X=[[1,7,3],[3,5,6],[6,8,9]]
Y=[[1,1,1,2],[6,7,3,0],[4,5,9,1]]
print(columns(X,Y))
print(multiply(X,Y))