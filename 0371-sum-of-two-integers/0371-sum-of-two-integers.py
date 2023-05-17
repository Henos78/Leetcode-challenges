class Solution:
    def getSum(self, a: int, b: int) -> int:
         # sum is obtained by getin the XOR adding a carry bit that is obtained by performing the AND (&) operation.
        #. not my solution must do it again!!
        mask = 0xFFFFFFFF
        
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)


        
        """ 
        while b:
            carry = a&b
            a = a ^b
            b = carry << 1
            
        return a
        
        got TLE solution for the input -1, 1"""