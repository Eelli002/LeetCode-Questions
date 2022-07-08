class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        start = 0
        s_table = {}
        
        for end in range(len(s)):
            while s[end] in s_table:
                s_table.pop(s[start])
                start += 1
            s_table[s[end]] = 1;
            length = max(length, end-start+1)
        return length