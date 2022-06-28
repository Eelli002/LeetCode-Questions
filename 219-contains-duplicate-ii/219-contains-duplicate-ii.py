class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_map = {}
        start = 0
        window_map[nums[start]] = 1
        for end in range(1, len(nums)):
            if abs(start - end) > k:
                window_map.pop(nums[start])
                start += 1
                
            if nums[end] in window_map: return True
            else: window_map[nums[end]] = 1
        return False