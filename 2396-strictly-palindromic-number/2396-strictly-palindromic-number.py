class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def helper(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n%b))
                n //= b
                
            return digits[::-1] == digits
        
        for i in range(2, n-1):
            if not helper(n,i):
                return False
            
        return True
        