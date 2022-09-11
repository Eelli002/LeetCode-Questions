class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome_str = ""
        for char in s:
            if char.isalnum():
                palindrome_str = palindrome_str + char
        palindrome_str = palindrome_str.lower()
        
        start = 0
        end = len(palindrome_str) - 1
        print(palindrome_str)
        
        while start <= end:
            if palindrome_str[start] != palindrome_str[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
        