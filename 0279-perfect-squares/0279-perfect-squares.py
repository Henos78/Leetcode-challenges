class Solution:
    def numSquares(self, n: int) -> int:
        psquare =[]
        
        for i in range(1,n+1):
            if int(i**0.5) == i**0.5:
                psquare.append(i) 
        
        dp = [float("inf")]*(n+1)
        
        # base case - amount assuming its 0
        dp[0] =0  # idx represent the amount
        
        for i in range(1,n+1):
            for num in psquare:
                temp = i-num
                if temp >=0:
                    dp[i] = min(dp[i], dp[temp])
            dp[i]+=1
            
        return dp[n] if dp[n] != float("inf") else -1