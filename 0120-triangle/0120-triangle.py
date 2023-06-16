class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # using bottom up appraoh
        dp = [triangle[0][0]] * len(triangle)
        
        for i in range(1, len(triangle)):
            triangle[i][i] += triangle[i-1][i-1]
            triangle[i][0] += triangle[i-1][0]
            
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
                
                
        res = min(triangle[-1])
        return res
        