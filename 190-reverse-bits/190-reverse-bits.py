class Solution:
    def reverseBits(self, n: int) -> int:
        new_str = 0
        
        for i in range(32):
            if (n&1):
                new_str = new_str << 1
                new_str = new_str | 1
                n = n >> 1
            else: 
                new_str = new_str << 1
                n = n >> 1
                
        return new_str
                