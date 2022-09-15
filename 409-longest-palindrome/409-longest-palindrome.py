class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        max_length = 0
        
        for i in char_count.values():
            max_length += int(i / 2) * 2
            
            if max_length % 2 == 0 and i % 2 == 1:
                max_length += 1
        return max_length