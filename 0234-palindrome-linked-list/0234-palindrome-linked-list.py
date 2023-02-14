# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numOfNodes = 0
        
        curr_node = head
        
        while curr_node:
            numOfNodes += 1
            curr_node = curr_node.next
            
        n = (numOfNodes // 2)-1

        curr_node = head
        prev_node = None
        
        for i in range(n+1):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        first_head = prev_node
                        
        if numOfNodes%2 == 0:
            second_head = curr_node
        else:
            second_head = curr_node.next
            
        while first_head and second_head:
            if first_head.val != second_head.val:
                return False
            first_head = first_head.next
            second_head = second_head.next
            
        return True

            
            
            
        
            