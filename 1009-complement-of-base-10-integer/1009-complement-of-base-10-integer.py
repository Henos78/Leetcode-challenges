class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n ==0:
            return 1
        
        res = 0
        i = 0 #idx
        while n:
    
            if n &1 == 0:
                 res |= 1 << i

            n >>= 1
            i+=1
            
        return res
        