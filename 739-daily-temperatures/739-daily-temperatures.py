class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        
        for idx, val in enumerate(temperatures):
                
            while stack and val > stack[-1][0]:
                stackVal, stackIdx = stack.pop()
                answer[stackIdx] = idx - stackIdx
            stack.append([val, idx])
        return answer
                