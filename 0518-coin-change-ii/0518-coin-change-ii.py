class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp =[0]*(amount+1)
        
        dp[0]=1
        
        for coin in coins:
            for i in range(coin, amount+1):
                temp = i-coin
                if temp>=0:
                    dp[i] +=dp[temp]
        print(dp)
        return dp[amount]
        
        