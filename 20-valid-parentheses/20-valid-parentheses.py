class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == '{':
                stack.append('{')
            elif s[i] == '[':
                stack.append('[')
                
            last = len(stack) - 1
            if len(stack) == 0:
                return False
            elif s[i] == ')':
                if stack[last] == '(':
                    stack.pop()
                else: return False
            elif s[i] == '}':
                if stack[last] == '{':
                    stack.pop()
                else: return False
            elif s[i] == ']':
                if stack[last] == '[':
                    stack.pop()
                else: return False
        
        if len(stack) == 0:
            return True