class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #dp with memoraization top down approach
        n = len(triangle)
        
        dp = [[-1]*len(triangle)  for _ in range(len(triangle))]
        
        def helper(i,j):
            # i-row and j - col
            if n-1 == i:
                return triangle[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]

            p1 = helper(i+1,j)
            p2 = helper(i+1,j+1)
            
            t1 = triangle[i][j] + p1
            t2 = triangle[i][j] + p2

            dp[i][j] = min(t1, t2)
            return dp[i][j]

        return helper(0,0)