# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            temp = curr
            ct = 1
            
            while temp.next and temp.val == temp.next.val:
                ct += 1
                temp = temp.next
                
            if ct > 1:
                if curr == head:
                    head = temp.next
                else:
                    prev.next = temp.next
                    
            else:
                prev = temp
                
            curr = temp.next
            
        return head
            
            
                
                
            
    
        