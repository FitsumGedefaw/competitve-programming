# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr_node = head
        prev_node = None
        first_end_node = ListNode()
        i = 1
        
        while curr_node:
            next_node = curr_node.next
            
            if prev_node:
                curr_node.next = prev_node
            
            if i == left-1:
                first_end_node = curr_node
                print(first_end_node.val)
            
            elif i >= left and i < right:
                prev_node = curr_node
                
            elif i == right:
                if left == 1:
                    head.next = next_node
                    head = curr_node
                    
                else:
                    first_end_node.next.next = next_node
                    first_end_node.next = curr_node
                    
                return head
            
            i += 1
            curr_node = next_node
                
        