class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < 0: nums[l] = abs(nums[l])
            if nums[r] < 0: nums[r] = abs(nums[r])
                
            if nums[l] < nums[r]:
                answer.append(nums[r]*nums[r])
                r -= 1
            else:
                answer.append(nums[l]*nums[l])
                l += 1
        answer.reverse()
        return answer