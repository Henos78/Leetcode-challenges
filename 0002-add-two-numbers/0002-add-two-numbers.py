# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        def changeArr(head): #change linked list to array
            arr = []
            cur = head
            
            while cur:
                arr.append(cur.val)
                cur = cur.next
            return arr
        
        def toLinked(arr): #change to linkedlist
            if not arr:
                return None
            head = ListNode(arr[0])
            curr = head
            for i in range(1, len(arr)):
                node = ListNode(arr[i])
                curr.next = node
                curr = node
            return head
        
        l11 = changeArr(l1)[::-1]
        l22 = changeArr(l2)[::-1]
        num1, num2 = "",""
        
        for num in l11:
            num1 += str(num)
        for num in l22:
            num2 +=  str(num)
        
            
        summ = [int(i) for  i in str(int(num1) +int(num2))][::-1]
        
        return toLinked(summ)