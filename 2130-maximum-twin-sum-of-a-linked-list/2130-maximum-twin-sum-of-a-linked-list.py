# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        
        while curr:
            #print("curr: ", curr)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        maxSum = float('-inf')
        while prev:
            #print("head= ", head, "prev= ", prev)
            maxSum = max(maxSum, head.val + prev.val)
            head =  head.next
            prev = prev.next
        
        return maxSum
        
        
        