# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        temp = head
        numOfNodes = 0
        
        while temp:
            numOfNodes += 1
            temp = temp.next
        #print("n: ", numOfNodes)
        
        k = k % numOfNodes
        #print("k: ", k)
        ct = 0
        curr = head
        prev = head
        cutPoint = ListNode()
        
        while curr:
            ct += 1
            if ct == numOfNodes - k:
                cutPoint = curr
                #print("cutpoint: ", cutPoint.val)
            prev = curr
            curr = curr.next
        
        if cutPoint.next:
            prev.next = head
            head = cutPoint.next
            cutPoint.next = None
        
        return head
                
        
        
        
        
        
        