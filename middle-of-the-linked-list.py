# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        item = head     #pointer 1
        count = 0
        while item != None:
            item = item.next
            count += 1
            
        node = head     #pointer 2
        if count % 2 != 0:  #total number of nodes is odd 
            index = -1
            while index < (count // 2) - 1:
                node = node.next
                index += 1
            return node
        else:       #total number of nodes is even 
            index = -1
            while index < (count / 2) - 1:
                node = node.next
                index += 1
            return node
            
            
