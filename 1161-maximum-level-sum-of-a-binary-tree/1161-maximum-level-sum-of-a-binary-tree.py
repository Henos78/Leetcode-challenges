# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q =deque([root])
        level = 0
        cur_level =0
        max_sum = float("-inf")
        
        while q:
            
            cur_level+=1
            cur_sum =0
            for _ in range(len(q)):
                cur = q.popleft()
                cur_sum += cur.val
               
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                    
            if cur_sum  > max_sum:
                level = cur_level
                max_sum=cur_sum
                
        return level
            
        
                