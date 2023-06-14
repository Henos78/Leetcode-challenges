class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # choose ds to store our answer
        dp = [float("inf")]*(amount+1)
        
        # base case - amount assuming its 0
        dp[0] =0  # idx represent the amount
        
        for i in range(1,amount+1):
            for coin in coins:
                temp = i-coin
                if temp >=0:
                    dp[i] = min(dp[i], dp[temp])
            dp[i]+=1
            
        return dp[amount] if dp[amount] != float("inf") else -1
            
        
        
        
        
        