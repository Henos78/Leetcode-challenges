# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        def changeArr(head):
            arr = []
            cur= head
            
            while cur:
                arr.append(cur.val)
                cur = cur.next
            return arr
        
        temp = changeArr(head)
        res=""
        for i in temp:
            res += str(i)
            
        return int(res,2)