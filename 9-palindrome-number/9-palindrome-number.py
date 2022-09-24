class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        
        left_divisor = 1
        while x >= left_divisor * 10:
            left_divisor *= 10

        while x:
            left = x  // left_divisor
            right = x % 10
            
            if left != right: return False
            
            x = (x % left_divisor) // 10
            
            left_divisor /= 100
        
        return True