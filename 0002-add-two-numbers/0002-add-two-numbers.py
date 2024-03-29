# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        
        curr = l1
        while curr:
            num1 = str(curr.val) + num1
            curr = curr.next
            
        curr = l2
        while curr:
            num2 = str(curr.val) + num2
            curr = curr.next
            
        #print("num1: ", num1, "num2: ", num2)
        
            
        _sum = str(int(num1) + int(num2))
       # print("sum: ", _sum)
        
        prev = None
        for digit in _sum:
            node = ListNode(int(digit))
            node.next = prev
            prev = node
        
        return prev
        
            
        
        