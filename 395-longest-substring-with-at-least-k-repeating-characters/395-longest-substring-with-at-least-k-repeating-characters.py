class Solution:
    def helper(self, s:str, start:int, end:int, k:int) -> int:
        if end - start < k: return 0
        
        s_table = Counter(s[start:end])
        
        for i in range(start, end):
            if s_table[s[i]] < k:
                j = i+1
                while j < end and s_table[s[j]] < k:
                    j+=1
                return max(self.helper(s, 0, i, k), self.helper(s, j, end, k))
        return end - start
    
    def longestSubstring(self, s: str, k: int) -> int:
        return self.helper(s, 0, len(s), k)