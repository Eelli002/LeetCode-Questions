class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) / 2
        char_count = {}
        
        for num in nums:
            if num in char_count:
                char_count[num] += 1
            else: char_count[num] = 1
            if char_count[num] >= majority:
                return num
        