# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        
        while curr:
            length += 1
            curr = curr.next
          
        n = length // 2
        i = 0
        curr = head

        
        while curr:
            if i == n:
                return curr
            i += 1
            curr = curr.next
            
        
        
        