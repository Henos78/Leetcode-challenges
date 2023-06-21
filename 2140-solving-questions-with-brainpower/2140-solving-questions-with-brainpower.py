class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #using bottom up
        n =len(questions)
        dp  =[-1]*n
        
        dp[-1] = questions[-1][0]
        
        for i in range(n-2,-1,-1):
            pick_idx =  i+questions[i][1]+1
            pick = questions[i][0]
            
            if pick_idx <n:
                pick += dp[pick_idx]
                
            not_pick = dp[i+1]
            
            dp[i] = max(pick,not_pick)
            
        return dp[0]
        
        