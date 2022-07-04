class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        idx = 0
        end = len(nums)-1
        
        while idx <= end and start < end:
            if nums[idx] == 0:
                nums[idx] = nums[start]
                nums[start] = 0
                start += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx] = nums[end]
                nums[end] = 2
                end -= 1
            else: idx += 1