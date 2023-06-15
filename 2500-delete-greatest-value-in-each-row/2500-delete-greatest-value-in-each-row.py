class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res= 0
        
        for i in range(n):
            maxx = 0
            for gri in grid:
                temp = max(gri)
                maxx =max(maxx,temp)
                gri.remove(temp)
            res+=maxx
        
        return res
            