# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level=0
        res= []
        q = deque([root])
        
        while q:
            level +=1
            summ= 0
            for _  in  range(len(q)):
                cur = q.popleft()
                summ += cur.val
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            res.append([level,summ])
                    
        res.sort(key = lambda x:x[1],reverse =True)
        return res[k-1][1] if len(res)>=k else -1
    
        