# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # implementation similar with Add Two Numbers (without reversing the input and res array)
        def changeArr(head):
            arr = []
            cur = head
            
            while cur:
                arr.append(cur.val)
                cur  =cur.next
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
        
        l11 = changeArr(l1)
        l22 = changeArr(l2)
        num1, num2 = "",""
        
        for num in l11:
            num1 += str(num)
        for num in l22:
            num2 +=  str(num)
        
        print(7243 + 564)
        summ = [int(i) for  i in str(int(num1) +int(num2))]
        
        return toLinked(summ)