'''
Given a string without spaces, the task is to remove duplicates from it.
Note: The original order of characters must be kept the same.
Input: "geeksforGeeks"
Output: geksfor
Explanation: Only keep the first
occurrence
'''

from collections import OrderedDict

def remove_duplicate(s):
    return "".join(OrderedDict.fromkeys(s))

s="geeksforgeeks"
print(remove_duplicate(s))
