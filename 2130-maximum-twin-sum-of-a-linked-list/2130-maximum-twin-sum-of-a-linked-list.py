# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        
        cur = head
        
        while cur is not None:
            arr.append(cur.val)
            cur = cur.next
            
        out = 0
        n = len(arr)

        for i in range(n):
            out =max(out, (arr[i]+ arr[n-i-1]))
        return out
        