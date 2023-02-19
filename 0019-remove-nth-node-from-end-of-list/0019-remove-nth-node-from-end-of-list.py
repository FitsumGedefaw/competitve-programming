# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        
        i = 1
        while fast:
            if i == n+1:
                break
            i += 1
            fast = fast.next
        
        if fast == None:
            return slow.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head
         
            