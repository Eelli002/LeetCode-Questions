class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_total = []
        t_total = []
        
        for char in s:
            if char == '#':
                if s_total: s_total.pop()
            else: s_total.append(char)
        print(s_total)
                
        for char in t:
            if char == '#':
                if t_total: t_total.pop()
            else: t_total.append(char)
        print(t_total)
                
        return True if s_total == t_total else False