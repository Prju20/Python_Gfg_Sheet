#Python - Convert Snake case to Pascal case 
"""
Input: geeks_for_geeks
Output: GeeksforGeeks

Input: left_index
Output:leftIndex

Method #1:Using title() + replace()
Method #2 : Using capwords() The task of performing title case is performed using capwords() in this method
Method #3 : Using split(),title() and join() methods
Approach#4:  Using capitalize
The function splits the input string into words based on the underscore separator, capitalizes the first letter of each word, and then concatenates the words to form the output string in PascalCase.
Algorithm
1. Split the given string at “_” to form a list of words.
2. Capitalize the first letter of each word and join them.
3. Return the resulting string in Pascal case.
"""
def Pascal(string):
    str=string.split("_")
    length=len(str)
    for i in range(0,length):
        str=str[i].capwords()
    return str

str="geeks_for_geeks"
print(Pascal(str))

