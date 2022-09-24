class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr_xor = 0
        for num in nums:
            arr_xor = arr_xor ^ num
        
        all_xor = 0
        for i in range(len(nums)+1):
            all_xor = all_xor ^ i
        
        return all_xor ^ arr_xor