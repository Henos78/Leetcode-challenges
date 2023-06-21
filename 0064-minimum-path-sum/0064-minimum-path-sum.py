class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        dp = [[float("inf") for _ in range(n+1)] for _ in range(m+1)]# here we initialise by adding additional row and col to compute the min value and wont go out of bounds.
        
        dp[m-1][n]= 0
        print(dp)
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
                
        return dp[0][0]
                
        