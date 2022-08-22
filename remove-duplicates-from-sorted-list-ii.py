# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            rearNode = head
            frontNode = head.next
            while frontNode and frontNode.next != None:
                if rearNode.val == frontNode.val:
                    temp = rearNode.val
                    while (frontNode.next) and (frontNode.next.val == temp):
                        frontNode = frontNode.next
                    if frontNode.next == None:
                        return None
                    else:
                        head = rearNode = frontNode.next
                        frontNode = rearNode.next
                elif frontNode.val == frontNode.next.val:
                    temp = frontNode.val
                    while (frontNode.next) and (frontNode.next.val == temp):
                        frontNode = frontNode.next
                    rearNode.next = frontNode.next
                    frontNode = rearNode.next
                else:
                    frontNode = frontNode.next
                    rearNode = rearNode.next
            if (head.next) and (head.next.next == None) and (head.val == head.next.val):
                return None
        return head
                    
                
        
            
