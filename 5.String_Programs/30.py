#Python | Replace all occurrences of a substring in a string
"""
Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd” 
Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str. 

Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd” 
Output : test_str = “geeksabcdgeeks”
"""
def test(string,s1,s2):
    input_string=string.replace(s1, s2)
    return input_string

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
print(test(test_str,s1,s2))
        