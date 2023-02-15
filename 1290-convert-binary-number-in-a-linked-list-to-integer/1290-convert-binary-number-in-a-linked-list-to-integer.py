# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binNum = ""
        curr_node = head
        
        while curr_node:
            binNum += str(curr_node.val)
            curr_node = curr_node.next
            
        return int(binNum, 2)