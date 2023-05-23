# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node at position left - 1
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sub-list from left to right
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next
        
        
        
        
        """
        Got wrong  answer for the input [3,5] l=1 r=2
        #convert to a list
        def changeArr(head):
            arr = []
            cur = head
            
            while cur:
                arr.append(cur.val)
                cur =cur.next
            return arr
        #to convert to linked list
        def toLinked(arr):
            if not arr:
                return
            head = ListNode(arr[0])
            cur = head
            
            for i in range(1, len(arr)):
                node = ListNode(arr[i])
                cur.next =node
                cur = node
                
            return head
        # to  reverse the values with in the segment: [left,right]
        def reverse(arr, l,r):
            if left < 0 or right >= len(arr) or left > right:
                return arr
            arr[left-1:right] = reversed(arr[left-1:right])

            return arr
        
        temp = changeArr(head)
        res = reverse(temp, left, right)
        print(res)
        return toLinked(res)
        """
        
        