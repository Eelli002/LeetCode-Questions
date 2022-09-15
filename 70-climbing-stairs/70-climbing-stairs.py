class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        n -= 1
        while n:
            temp = a
            a = b+a
            b = temp
            n -= 1
        return a