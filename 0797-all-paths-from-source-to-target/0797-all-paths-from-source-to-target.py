class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        #Idea from the discussion using dfs
        
        res = []
        stack = [(0, [0])]
        n = len(graph)-1
        
        while stack:
            cur, route = stack.pop()
            if cur == n:
                res.append(route)
            else:
                for node in graph[cur]:
                    stack.append((node, route + [node]))
                    
        return res
            
        
        
        
        