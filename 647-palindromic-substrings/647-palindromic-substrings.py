class Solution:
    def countSubstrings(self, s: str) -> int:
        num_of_pali = 0
        
        for char in range(len(s)):
            start = end = char
            while start >= 0 and end < len(s) and s[start] == s[end]:
                num_of_pali += 1
                start -= 1
                end += 1
            
            start = char
            end = char + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                num_of_pali += 1
                start -= 1
                end += 1
        return num_of_pali