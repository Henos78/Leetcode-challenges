# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #dfs appraoch and solution
        self.res = float("inf")
        self.prev =None
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.prev is not None:
                self.res  = min(self.res,abs(node.val- self.prev))
            self.prev = node.val
            
            dfs(node.right)
            
        dfs(root)
        return self.res
        
        """
        #trail using bfs didnt work
        res =  float("inf")
        q = deque([root])
        
        while q:
            
            for _ in range(len(q)):
                cur = q.popleft()
                diff = float("inf")
                
                if cur.left:
                    q.append(cur.left)
                    diff = min(diff,abs(cur.val-cur.left.val))
                if cur.right:
                    q.append(cur.right)
                    diff = min(diff,abs(cur.val-cur.right.val))
                    
            res= min(res, diff)
            
        return res
        """
        