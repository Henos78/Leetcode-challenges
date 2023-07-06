class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        xor = bin(x^y)[2:]
        
        for i in xor:
            res+= int(i)
    
        return res