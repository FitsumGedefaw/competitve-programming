# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepthHelper(self, root):
        if root == None:
            return 0
        
        depth1 = self.maxDepthHelper(root.left)
        depth2 = self.maxDepthHelper(root.right)
        
        return max(depth1, depth2) + 1
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root)
        
        