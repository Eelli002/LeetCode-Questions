class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_shift = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_shift += 1
                
            else:
                nums[i - zero_shift] = nums[i]
                
        for idx in range(len(nums)-zero_shift, len(nums)):
            nums[idx] = 0
        print(nums)
                