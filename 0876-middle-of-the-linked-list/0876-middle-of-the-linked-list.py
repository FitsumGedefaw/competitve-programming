# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoize = head
        rabbit = head
        
        while rabbit and rabbit.next:
            rabbit = rabbit.next.next
            tortoize = tortoize.next
            
        return tortoize