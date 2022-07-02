class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        answer = [0] * n
        
        
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                stackVal, stackIdx = stack.pop()
                answer[stackIdx] = i - stackIdx
            stack.append([v, i])
        return answer
                
            
        
        
        
        return answer
#         for i in range(n):
#             answer.append(0)
#             if len(t_stack) == 0: t_stack.append(temperatures[i])
#             else:
#                 while t_stack and temperatures[i] > t_stack[len(t_stack)-1]:
#                     index = temperatures.index(t_stack[len(t_stack)-1])
#                     answer[index] = i - index - 1
#                     t_stack.pop()
#                 t_stack.append(temperatures[i])
            
#         return answer
        