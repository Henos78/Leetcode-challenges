class Solution:
    def getSum(self, a: int, b: int) -> int:
       #neetcode solution
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:  # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:  # -a == b
                return 0
            if add(~a, 1) < b:  # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

        return add(a, b)
        
        
        
        
        
        """
         # sum is obtained by getin the XOR adding a carry bit that is obtained by performing the AND (&) operation.
        
        #works for positive integers not for the summation of negative and positive 
        while b !=0:
            carry = (a&b) <<1
            a = a^b
            b = carry
        return a
         """