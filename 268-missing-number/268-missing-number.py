class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_of_n = ( (n) * (n+1) ) // 2
        sum_of_nums = 0
        for num in nums:
            sum_of_nums += num
        return sum_of_n - sum_of_nums