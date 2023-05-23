# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #using bit o(1) space compelxity
        res = ""
        cur = head
        while cur:
            res += str(cur.val)
            cur = cur.next
        
        num =0
        for i in res:
            num = num << 1
            if i == '1':
                num |=1
        return num

        