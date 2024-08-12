#Python Program for Matrix Product
"""
Input: [[1,4,5],[7,3],[4],[46,7,3]]
Output: 1622880
"""
def multiply(mat):
    multiply=1
    length=len(mat)
    for i in range(0,length):
        width=len(mat[i])
        for j in range(0,width):
            multiply*=mat[i][j]
    return multiply

mat= [[1,4,5],[7,3],[4],[46,7,3]]
print(multiply(mat))