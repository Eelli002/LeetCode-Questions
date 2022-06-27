class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_subarray = len(nums) + 1
        window_start = 0
        curr_count = 0
        
        for i in range(len(nums)):
            curr_count += nums[i]
            while curr_count >= target:
                min_subarray = min(min_subarray, i - window_start + 1)
                curr_count -= nums[window_start]
                window_start += 1
            
            
        if min_subarray == len(nums) + 1:
            min_subarray = 0
        return min_subarray