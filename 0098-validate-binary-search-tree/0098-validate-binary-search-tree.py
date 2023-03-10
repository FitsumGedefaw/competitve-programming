# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validateHelper(self, currNode, newMin, newMax):
        if not currNode:
            return True
        
        if currNode.val < newMax and currNode.val > newMin:
            return self.validateHelper(currNode.left, newMin, currNode.val) and self.validateHelper(currNode.right, currNode.val, newMax)
        
        return False
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateHelper(root, float('-inf'), float('inf'))
        