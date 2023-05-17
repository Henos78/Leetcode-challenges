class Solution:
    def findComplement(self, num: int) -> int:
        # using purely bits
        res = 0
        i = 0 #idx
        while num:
            if num &1 == 0:
                 res |= 1 << i

            num >>= 1
            i+=1
            
        return res