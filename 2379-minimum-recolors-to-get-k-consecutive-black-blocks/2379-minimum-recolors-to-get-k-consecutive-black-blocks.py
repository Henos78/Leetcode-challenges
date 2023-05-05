class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = 100 #Since the constraint is 100, we wanted to make it the maximum possible
        l,r =0,0
        cnt =0
        
        for r in range(len(blocks)):
            if blocks[r] =='W':
                cnt +=1
                
            if (r-l) == k-1:
                ans = min(ans,cnt)
                
                if blocks[l] == 'W':
                    cnt -= 1
                l +=1
                
        return ans
        
    