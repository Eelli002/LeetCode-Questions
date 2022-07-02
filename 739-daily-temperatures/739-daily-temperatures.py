class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n
        
        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackVal, stackIdx = stack.pop()
                answer[stackIdx] = idx - stackIdx
            stack.append([val, idx])
        return answer     