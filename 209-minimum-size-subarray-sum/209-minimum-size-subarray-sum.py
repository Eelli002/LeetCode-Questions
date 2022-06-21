class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = j = total = 0
        min_len = n+1
        s = 0
        array = []
        while j < n:
            s = s + nums[j]
            array.append(s)
            total = array[j]
            if total >= target:
                while i <= j and total >= target:
                    min_len = min(min_len, j-i+1)
                    total = array[j] - array[i]
                    i += 1
            j += 1
        return min_len if min_len != n+1 else 0