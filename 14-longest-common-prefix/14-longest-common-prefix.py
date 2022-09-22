class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        
        for i in range(len(strs[0])):
            for elem in strs:
                if i == len(elem) or elem[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
            
        return prefix