class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = curr = 0
        
        for num in nums:
            if num == curr:
                count += 1
            else:
                if count == 0:
                    curr = num
                    count += 1
                else: count -= 1
        return curr