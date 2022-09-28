class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = []
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] * nums[l] < nums[r] * nums[r]:
                answer.append(nums[r]*nums[r])
                r -= 1
            else:
                answer.append(nums[l]*nums[l])
                l += 1
        return answer[::-1]