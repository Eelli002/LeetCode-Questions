class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindrome_str = ""
        # for char in s:
        #     if char.isalnum():
        #         palindrome_str = palindrome_str + char
        # palindrome_str = palindrome_str.lower()
        
        start = 0
        end = len(s) - 1
        
        while start < end:
            if not s[start].isalnum():start += 1
            elif not s[end].isalnum():end -= 1
            elif s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else: return False
        return True
        