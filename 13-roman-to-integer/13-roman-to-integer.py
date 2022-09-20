class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_map = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        special_map = ['I', 'X', 'C']
        int_total = 0
        
        curr = checker = 0
        while curr < len(s):
            if s[curr] in special_map and curr+1 < len(s):
                if numeral_map[ s[curr+1] ] > numeral_map[s[curr]]:
                    int_total += numeral_map[ s[curr+1] ] - numeral_map[s[curr]]
                    curr += 2
                else:
                    int_total += numeral_map[s[curr]]
                    curr += 1
            else:
                int_total += numeral_map[s[curr]]
                curr += 1
        return int_total