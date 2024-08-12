#Transpose a matrix in Single line in Python
"""
Input: [[1,2],[3,4],[5,6]]
Output: [[1,3,5],[2,4,6]]
Explanation: Suppose we are given a matrix
                       [[1, 2],
                        [3, 4],
                        [5, 6]]
Then the transpose of the given matrix will be, 
                       [[1, 3, 5],
                        [2, 4, 6]]
"""
def transpose(mat):
    length=len(mat)
    width=len(mat[0])
    for i in range(0,length):
        for j in range(0,width):
            

    return mat
            

        


mat=[[1,2],[3,4],[5,6]]
print(transpose(mat))