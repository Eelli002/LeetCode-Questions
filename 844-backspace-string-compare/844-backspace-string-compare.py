class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_total = ''
        t_total = ''
        
        for char in s:
            if char == '#':
                s_total = s_total[:-1]
            else: s_total = s_total + char
                
        for char in t:
            if char == '#':
                t_total = t_total[:-1]
            else: t_total = t_total + char
                
        return True if s_total == t_total else False