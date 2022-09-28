class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_sum = ~sys.maxsize
        curr_sum = 0
        
        for num in nums:
            if curr_sum < 0: curr_sum = 0
            curr_sum += num
            total_sum = max(total_sum, curr_sum)
            
        return total_sum