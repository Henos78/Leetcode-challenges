class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res= 0

        m = len(grid)
        columns =[]
        for col in range(m):
            temp = []
            for row in range(m):
                val = grid[row][col]
                temp.append(val)
            columns.append(temp)
    
        for col in columns:
            for i in range(m):
                if grid[i]==col:
                    res+=1
                        
        return res
            
            
            