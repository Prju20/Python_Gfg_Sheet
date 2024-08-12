#Python | Check if a Substring is Present in a Given String
"""
Input: Substring = "geeks"
        Strings="geeks for geeks"
Output: yes
Input: Substring = "geek"
        String="geeks for geeks"
Output: yes
Explanation: In this, we are checking if the substring is present in a given string or not.
"""
def substring(string,substring):
    str=string.split()
    number=len(string)
    for i in range(0,number):
        if substring==str[i]:
            return "Yes"
    return "No"


string="geeks for geeks"
sub="geeks"
print(substring(string,sub))


    