# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedHead = ListNode()
        sortedHead.next = head
        sortedTail = head
        curr = head.next
        
        while curr:
            if curr.val >= sortedTail.val:
                sortedTail = curr
            
            else:
                sortedTail.next = curr.next
                insertPos = sortedHead
                
                while insertPos.next.val <  curr.val:
                    insertPos = insertPos.next
                
                curr.next = insertPos.next
                insertPos.next = curr
                
            curr = sortedTail.next
            
        return sortedHead.next
                
                
                
                
        