class Solution:
    def hammingWeight(self, n: int) -> int:
        count = Counter(str(bin(n)))
        return count['1']