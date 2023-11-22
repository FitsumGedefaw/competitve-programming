# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        middleNode = self.extractMiddle(head)
        node = TreeNode(middleNode.val)
        node.right = self.sortedListToBST(middleNode.next)
        middleNode.next = None
        node.left = self.sortedListToBST(head)

        return node

    def extractMiddle(self, startNode):
        slow = startNode
        fast = startNode
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None # break the link
        return slow 
            
            


        