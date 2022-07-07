class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_length = len(p)
        start = 0
        p_table = Counter(p)
        s_table = {}
        starting_idx = []
        
        for end in range(len(s)):
            if s[end] in s_table: s_table[s[end]] += 1
            else: s_table[s[end]] = 1
            print(s_table)
            if end-start+1 == window_length:
                if s_table == p_table: starting_idx.append(start)
                if s_table[s[start]] > 1: s_table[s[start]] -= 1
                else: s_table.pop(s[start])
                start += 1
        return starting_idx