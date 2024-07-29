#Python | Sort the values of first list using second list
"""
Input : list1 = [“a”, “b”, “c”, “d”, “e”, “f”, “g”, “h”, “i”]
           list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
Output : [‘a’, ‘d’, ‘h’, ‘b’, ‘c’, ‘e’, ‘i’, ‘f’, ‘g’]

Input : list1 = [“g”, “e”, “e”, “k”, “s”, “f”, “o”, “r”, “g”, “e”, “e”, “k”, “s”]
            list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
Output : [‘g’, ‘k’, ‘r’, ‘e’, ‘e’, ‘g’, ‘s’, ‘f’, ‘o’]

Zip the two lists.
Create a new, sorted list based on the zip using sorted().
Using a list comprehension extract the first elements of each pair from the sorted, zipped list.
USe zip() function
"""