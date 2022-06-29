class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_table = {}
        length = -sys.maxsize
        start = 0
        
        for end in range(len(s)):
            while s[end] in s_table:
                s_table.pop(s[start])
                start += 1
            s_table[s[end]] = 1
            length = max(length, end-start+1)
        return 0 if length == -sys.maxsize else length
            
            
        