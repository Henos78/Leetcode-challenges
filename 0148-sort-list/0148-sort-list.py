# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def changeArr(head):
            arr= []
            cur = head
            
            while cur:
                arr.append(cur.val)
                cur = cur.next
            return arr
        
        def toLinked(arr):
            
            if not arr:
                return
            head = ListNode(arr[0])
            cur = head

            for i in range(1, len(arr)):
                node = ListNode(arr[i])
                cur.next = node
                cur = node
            return head
        
        res = sorted(changeArr(head))
        # res.sort()

        return toLinked(res)