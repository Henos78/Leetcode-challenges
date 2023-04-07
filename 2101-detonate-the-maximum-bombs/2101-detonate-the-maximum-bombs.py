class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for i in range(n)]
        maxbomb = 0
        visited = set()
        
        for i in range(n):
            x1, y1, r1 =bombs[i]
            for j in range(n):
                if i ==j:
                    continue
                x2, y2, r2 = bombs[j]
                dist = (x1-x2)**2 + (y1-y2)**2
                
                if dist <= r1**2:
                    graph[i].append(j)
    
        def dfs(node):
            visited.add(node)
            if not graph[node]:
                return 1
            
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        
        
        for i in range(n):
            dfs(i)
            maxbomb = max(maxbomb, len(visited))
            visited = set()
            
        return maxbomb
            
            
        