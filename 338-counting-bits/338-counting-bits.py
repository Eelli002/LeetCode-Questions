class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(0, n+1, 1):
            one_count = 0
            bin_str = str(bin(i))
            for char in bin_str:
                if char == '1': one_count += 1
            answer.append(one_count)
            
        return answer