class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        #define the DSA for the answer
        m ,n = len(grid), len(grid[0])
        dp =[[0 for _ in range(n+1)] for  _ in range(m+1)]
        
        dp[m-1][n]=1
        
        def bound(i,j):
            if 0<=i<m and 0<=j<n:
                return dp[i][j]
            return 0
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if grid[row][col]==0:
                    dp[row][col] += dp[row+1][col]+dp[row][col+1]
  
                   
        return dp[0][0]
        