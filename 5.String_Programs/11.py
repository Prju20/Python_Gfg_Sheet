#Python | Count the Number of matching characters in a pair of string
"""
Input: str1 = 'abcdef'
       str2 = 'defghia'
Output: 4
(i.e. matching characters :- a,d,e,f)

Input: str1='aabcddekll12@'
       str2='bb2211@55k'
Output: 5
(i.e. matching characters :- b,1,2,@,k)
"""
def match(str1,str2):
    len1=len(str1)
    len2=len(str2)
    count=0
    for i in range(0,len1):
       for j in range(0,len2):
           if str1[i]==str2[j]:
              count+=1
              break      
    return count

str1 = 'abcdef'
str2 = 'defghia'
#str1='aabcddekll12@'
#str2='bb2211@55k'
print(match(str1,str2))
           
            