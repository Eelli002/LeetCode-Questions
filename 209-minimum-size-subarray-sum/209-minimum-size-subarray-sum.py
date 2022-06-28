class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = sys.maxsize
        curr_count = 0
        start = 0
        for end in range(len(nums)):
            curr_count += nums[end]
            while curr_count >= target:
                min_length = min(min_length, end-start+1)
                curr_count -= nums[start]
                start += 1
                
        return 0 if min_length == sys.maxsize else min_length