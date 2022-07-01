class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_table = defaultdict(int)
        start = 0
        length = 0
        
        for end in range(len(s)):
            s_table[s[end]] += 1
            while s_table[s[end]] > 1:
                s_table[s[start]] -= 1
                if s_table[s[start]] == 0:
                    del s_table[s[start]]
                start += 1
            length = max(length, end-start+1)
        return length
        