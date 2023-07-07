class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l,r=0, int(c**0.5)
        
        while l<=r:
            tmp = l**2 + r**2
            
            if tmp ==c:
                return True
            if tmp<c:
                l+=1
            else:
                r -=1
                
        return False
            