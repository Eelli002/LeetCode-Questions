class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max = nums[0]
        curr_total = 0
        
        for num in nums:
            if curr_total < 0:
                curr_total = 0
            curr_total += num
            total_max = max(total_max, curr_total)
                
        return total_max