#Python - Vertical Concatenation in Matrix
"""
nput : [[“Gfg”, “good”], [“is”, “for”]] 
Output : [‘Gfgis’, ‘goodfor’] 
Explanation : Column wise concatenated Strings, “Gfg” concatenated with “is”, and so on. 

Input : [[“Gfg”, “good”, “geeks”], [“is”, “for”, “best”]] 
Output : [‘Gfgis’, ‘goodfor’, “geeksbest”] 
Explanation : Column wise concatenated Strings, “Gfg” concatenated with “is”, and so on.
"""
def join(matrix):
    lenth=len(matrix)
    mat=[]
    for i in range(0,lenth):
        for j in range(0,lenth):
            matrix[i][j]=mat[i][j]+mat[lenth-1][j]
    return mat

mat=[["Gfg","good"],["is","for"]]
print(join(mat))