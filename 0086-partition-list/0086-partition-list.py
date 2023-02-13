# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = ListNode()
        larger_head = ListNode()
        
        smaller_end_node = smaller_head
        larger_end_node = larger_head

        curr_node = head
        
        while curr_node:
            if curr_node.val < x:
                smaller_end_node.next = curr_node
                smaller_end_node = curr_node
                
            else:
                larger_end_node.next = curr_node
                larger_end_node = curr_node
                
            curr_node = curr_node.next
            
        larger_end_node.next = None
        
        smaller_end_node.next = larger_head.next
        
        return smaller_head.next
            
        
            