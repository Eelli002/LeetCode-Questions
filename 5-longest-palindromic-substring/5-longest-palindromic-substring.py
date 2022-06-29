class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        
        for i in range(len(s)):
            start = end = i
            curr_str = ""
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if start == end: curr_str = s[start]
                else: curr_str = s[start] + curr_str + s[end]
                if len(substring) < len(curr_str): substring = curr_str
                start -= 1
                end += 1
                
            start = i
            end = i+1
            curr_str = ""
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end+1 == start: curr_str = s[start] + s[end]
                else: curr_str = s[start] + curr_str + s[end]
                if len(substring) < len(curr_str): substring = curr_str
                start -=1
                end += 1
        return substring