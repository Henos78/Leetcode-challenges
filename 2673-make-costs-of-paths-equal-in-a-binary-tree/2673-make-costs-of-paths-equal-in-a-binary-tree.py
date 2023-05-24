class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.res = 0
        def dfs(node):
            if node >=n:
                return 0
            
            lnode = dfs(node * 2 + 1)
            rnode = dfs(node * 2 + 2)
            
            if lnode != rnode:
                self.res += abs(rnode - lnode)
                
            return cost[node] + max(lnode, rnode)
        
        
        dfs(0)
        return self.res
        