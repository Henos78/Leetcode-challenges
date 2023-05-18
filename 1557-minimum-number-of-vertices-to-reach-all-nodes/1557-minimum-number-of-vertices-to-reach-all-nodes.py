class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # another solution (idea taken from others )
        indegree = [0] * n
        for edge in edges:
            indegree[edge[1]] += 1

        res = []
        for i in range(n):
            if indegree[i] == 0:
                res.append(i)

        return res
    
        """
        # had an error for some test cases
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)

        # Perform dfs starting from any node
        visited = [False] * n
        def dfs(node):
            visited[node] = True
            for neighbor in adjList[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        res = []
        # Traverse all nodes
        for u in range(n):
            if not visited[u]:
                res.append(u)
                dfs(u)

        return res
        """