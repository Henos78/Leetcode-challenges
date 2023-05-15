# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #brute force with t.c of o(n)
        
    # convert the linked list. onto an array
        def changeArr(head):
            arr = []
            cur = head

            while cur:
                arr.append(cur.val)
                cur = cur.next
            return arr
        
        #convert back to a linked list
        def toLinkedlist(arr):
            if not arr:
                return None
            head = ListNode(arr[0])
            curr = head
            for i in range(1, len(arr)):
                node = ListNode(arr[i])
                curr.next = node
                curr = node
            return head
        
        temp = changeArr(head)
        
        temp[k-1], temp[len(temp)-k] = temp[len(temp)-k], temp[k-1]
            
        return toLinkedlist(temp)
