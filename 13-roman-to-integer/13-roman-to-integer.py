class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_map = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        int_total = curr = 0

        while curr < len(s):
            if curr+1 < len(s) and numeral_map[s[curr]] < numeral_map[s[curr+1]]:
                int_total += numeral_map[ s[curr+1] ] - numeral_map[s[curr]]
                curr += 2
            else:
                int_total += numeral_map[s[curr]]
                curr += 1
        return int_total