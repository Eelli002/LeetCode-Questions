class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num in count:
            if count[num] != 2: return num