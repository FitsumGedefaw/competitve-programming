# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode()
        even_head = ListNode()
        
        odd_tail = odd_head
        even_tail = even_head
        
        i = 1
        curr = head
        while curr:
            if i % 2 != 0:
                odd_tail.next = curr
                odd_tail = odd_tail.next
                
            else:
                even_tail.next = curr
                even_tail = even_tail.next
             
            i += 1
            curr = curr.next
        
        odd_tail.next = even_head.next
        even_tail.next = None
        
        return odd_head.next
        
            
            
            