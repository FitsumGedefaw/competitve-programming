# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
            
        return arr[len(arr)//2]