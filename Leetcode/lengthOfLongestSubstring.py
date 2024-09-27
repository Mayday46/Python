class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = []  # to store the lengths of valid substrings
        left = 0  # left pointer to track the start of the window
        temp = ''  # temporary substring without repeating characters

        while left < len(s):
            if s[left] not in temp:
                temp += s[left]  # add the character to the current substring
                left += 1  # move the left pointer forward
            else:
                # found a duplicate, save the current substring length
                ans.append(len(temp))
                # move the window by removing characters up to the first occurrence of the duplicate
                # keep the remaining part of `temp` after the first duplicate
                temp = temp[temp.index(s[left]) + 1:]
        
        # Append the last valid substring length if `temp` is non-empty
        ans.append(len(temp))
        
        return max(ans)  # return the length of the longest valid substring
