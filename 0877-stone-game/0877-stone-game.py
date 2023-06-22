class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #solve again using using bottom up dp
        dp = {}
        
        def solve(i,j):
            if i==j:
                return piles[i]
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            #option1 start from the first
            choose1 = piles[i]  - solve(i+1,j)
            #option2 choose from the last
            choose2 = piles[j]- solve(i,j-1)
            
            dp[(i,j)] = max(choose1, choose2)
            
            return dp[(i,j)]
        
        return solve(0, len(piles)-1)>0
            
        
            

        
            