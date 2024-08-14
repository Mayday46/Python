

'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 2:
    Input: s = "(]"
    Output: false

'''

class Solution:
    def isValid(self, s: str) -> bool: # Brute Force Apporach
        reference = {'(': ')', '{': '}', '[': ']'}
        pointer1 = 0
        size = len(s) - 1

        while pointer1 < size:
            
            if s[pointer1] in reference and reference[s[pointer1]] == s[pointer1 + 1]:
                # Found a pair
                s = s[:pointer1] + s[pointer1 + 2:]
                pointer1 = 0
            else:
                pointer1 += 1
        
        return len(s) == 0