class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        
        while start <= end:
            midpoint = int(start + ((end - start) / 2))
            if target < nums[midpoint]:
                end = midpoint - 1
            elif target > nums[midpoint]:
                start = midpoint + 1
            else: return midpoint
        return -1
        
        
        
        
        
        
        
        # while midpoint >= 0 and midpoint < len(nums):
        #     print(midpoint)
        #     if target < nums[midpoint]:
        #         nums = nums[:midpoint-1]
        #         print(nums)
        #         midpoint = int((len(nums)-1) / 2)
        #     elif target > nums[midpoint]:
        #         nums = nums[midpoint+1:len(nums)]
        #         print(nums)
        #         midpoint = int((len(nums)-1) / 2)
        #     else: return midpoint
        # return -1
        