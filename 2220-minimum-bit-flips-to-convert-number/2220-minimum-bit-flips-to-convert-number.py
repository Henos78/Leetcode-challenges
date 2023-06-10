class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res =0
        
        while start or goal:
            a = start&1
            b = goal&1
            
            if a != b:
                res += a|b
            
            start >>=1
            goal >>= 1
            
        return res