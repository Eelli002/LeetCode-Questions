class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = ''
        carry = 0
        
        a, b = a[::-1], b[::-1]
        
        for i in range(max(len(a), len(b) )):
            char_a = ord(a[i]) - ord('0') if i < len(a) else 0
            char_b = ord(b[i]) - ord('0') if i < len(b) else 0
            
            total = char_a + char_b + carry
            char_sum = str(total % 2)
            answer = char_sum + answer
            carry = total //2
            
        if carry: answer = '1' + answer
            
        return answer