# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        end_node = head
        
        curr1 = list1
        curr2 = list2
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                end_node.next = curr1
                end_node = end_node.next
                curr1 = curr1.next
                
            else:
                end_node.next = curr2
                end_node = end_node.next
                curr2 = curr2.next
                
        while curr1:
            end_node.next = curr1
            end_node = end_node.next
            curr1 = curr1.next
            
        while curr2:
            end_node.next = curr2
            end_node = end_node.next
            curr2 = curr2.next
            
        return head.next
            
            
        
            
                
                
    