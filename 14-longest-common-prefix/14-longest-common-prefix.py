class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        shortest_length = 201
        
        for i in range(len(strs)):
            if len(strs[i]) < shortest_length:
                shortest_length = len(strs[i])
                shortest = strs[i]
        
        for idx in range(shortest_length):
            for elem in strs:
                if elem[idx] != shortest[idx]:
                    return prefix
            prefix += shortest[idx]
            
        return prefix