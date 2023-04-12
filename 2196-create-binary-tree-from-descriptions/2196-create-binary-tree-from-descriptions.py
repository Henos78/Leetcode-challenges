# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Here first we build the graph
        graph = defaultdict(set)
        All = set()
        hasParent = set()
        
        for p, c, isLeft in descriptions:
            graph[p].add((c, isLeft))
            All.add(p)
            All.add(c)
            hasParent.add(c)
        
        # Here we find the root of the node
        root = None
        
        for node in All:
            if node not in hasParent:
                root = TreeNode(node)
                break
                
        # By using simple dfs we build the graph
        
        def dfs(parent):
            for c, isLeft in graph[parent.val]:
                if isLeft:
                    parent.left = TreeNode(c)
                    dfs(parent.left)
                else:
                    parent.right = TreeNode(c)
                    dfs(parent.right)
                    
        dfs(root)
        return root
        
        