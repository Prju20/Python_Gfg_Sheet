#Python - Least Frequent Character in String
"""
Input:GeeksforGeeks
Output: f

Naive method + min() 
In this method, we simply iterate through the string and form a key in a dictionary of newly occurred element or if element is already occurred, we increase its value by 1. We find minimum occurring character by using min() on values. 

Method 2 : Using collections.Counter() + min() 
"""