#Ways to remove i'th character from string in Python
"""
Input: 'Geeks123For123Geeks'
Output: GeeksForGeeks
Explanation: In This, we have removed the '123' character from a string.
"""
def findNumber(string):
    length=len(string)
    str=""
    for i in range(0,length):
        if string[i]==int:
            del(string[i])
        else:
            str=str+string[i]
    return str

Input="Geeks123For123Geeks"
print(findNumber(Input))
