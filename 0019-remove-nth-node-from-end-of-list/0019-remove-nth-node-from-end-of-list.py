# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head 
        
        while curr:
            sz += 1
            curr = curr.next
            
        n = sz - n
        
        if n == 0:
            return head.next
        
        else:
            curr = head
            i = 1
            
            while curr:
                if i == n:
                    curr.next = curr.next.next
                    return head
                curr = curr.next
                i += 1
        
                

            
        
        