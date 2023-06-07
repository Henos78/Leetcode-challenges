class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @lru_cache
        def helper(i,j):
            # i-row and j - col
            if n-1 == i:
                return triangle[i][j]

            p1 = helper(i+1,j)
            p2 = helper(i+1,j+1)
            
            t1 = triangle[i][j] + p1
            t2 = triangle[i][j] + p2

            return min(t1, t2)

        return helper(0,0)