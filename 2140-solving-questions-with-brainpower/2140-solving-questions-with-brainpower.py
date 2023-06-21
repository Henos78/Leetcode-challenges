class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #using top down
        dp  =[-1]*len(questions)
        
        def solve(i):
            if i>=len(questions):
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            pick = questions[i][0] + solve(i+questions[i][1]+1)
            not_pick = solve(i+1)
            dp[i]=max(pick,not_pick)
                         
            return dp[i]
      
        return solve(0)
            
        
        