class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = False
        bin_sum = ''
        while a and b:
            if a[-1] == '1' and b[-1] == '1':
                if carry:
                    bit = '1'
                else:
                    bit = '0'
                    carry = True
                    
            elif (a[-1] == '1' and b[-1] == '0') or (a[-1] == '0' and b[-1] == '1'):
                if carry: 
                    bit = '0'
                else:
                    bit = '1'
                    
            else:
                if carry:
                    bit = '1'
                    carry = False
                else: bit = '0'
            bin_sum = bit + bin_sum
            a = a[:-1]
            b = b[:-1]
        
        print('curr sum: ', bin_sum)
        
        while a:
            print('starting a')
            if a[-1] == '1':
                print('a')
                if carry:
                    bit = '0'
                else:
                    bit = '1'
            else:
                print('b')
                if carry:
                    bit = '1'
                    carry = False
                else: bit = '0'
            bin_sum = bit + bin_sum
            a = a[:-1]
        
        while b:
            print('starting b')
            if b[-1] == '1':
                if carry:
                    bit = '0'
                else:
                    bit = '1'
            else:
                if carry:
                    bit = '1'
                    carry = False
                else: bit = '0'
            bin_sum = bit + bin_sum
            b = b[:-1]

        if carry: bin_sum = '1' + bin_sum
            
        return bin_sum