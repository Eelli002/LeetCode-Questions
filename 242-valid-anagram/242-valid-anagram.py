class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_table_s = {}
        char_table_t = {}
        
        for char in s:
            if char in char_table_s: char_table_s[char] += 1
            else: char_table_s[char] = 1
        
        for char in t:
            if char in char_table_t: char_table_t[char] += 1
            else: char_table_t[char] = 1
                
        return True if (char_table_s == char_table_t) else False