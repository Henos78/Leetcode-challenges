class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res =0
        
        for gri in grid:
            for i in range(len(gri)):
                if gri[i] <0:
                    res +=1
        return res
    # o(n^2)
        