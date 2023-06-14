class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #using bottum up dp
        #step one chose a data Structure to store my result
        dp =[[0 for _  in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1
        #S2: state transtion
        #check if it is out of bounds to return 0 if they are
        
        def bound(i,j): #helps to check the edges
            if 0<=i<m and 0<=j<n:
                return dp[i][j]
            return 0
                
            
        #s3: build
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                dp[row][col] += bound(row+1,col) + bound(row,col+1)
                
        return dp[0][0]
        