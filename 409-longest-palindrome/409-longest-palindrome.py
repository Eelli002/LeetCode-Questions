class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_length = 0
    
        char_count = {}
        for char in s:
            if char in char_count: char_count[char] += 1
            else: char_count[char] = 1
        
        odd_count = 1
        
        for char in s:
            if (char_count[char] % 2) == 1:
                if char_count[char] > 1:
                    max_length += 2
                    char_count[char] -= 2
                elif odd_count:
                    odd_count -= 1;
                    char_count[char] -= 1
                    max_length += 1
            elif (char_count[char] % 2) == 0:
                max_length += char_count[char]
                char_count[char] -= char_count[char]
        
        return max_length
                