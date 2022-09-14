# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end, first_bad = 1, n, n
        while start <= end:
            midpoint = int((start + end) / 2)
            if isBadVersion(midpoint):
                first_bad = midpoint
                end = midpoint - 1
            else: start = midpoint + 1
        return first_bad