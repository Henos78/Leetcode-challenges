class Solution:
    def countBits(self, n: int) -> List[int]:
        # now using right shifting operation
        res = []
        
        for i in range(n+1):
            ans = 0
            while i >0:
                
                if i &1 ==1:
                    ans +=1
                    
                i >>= 1
                
            res.append(ans)
            
        return res
        
        
        
        