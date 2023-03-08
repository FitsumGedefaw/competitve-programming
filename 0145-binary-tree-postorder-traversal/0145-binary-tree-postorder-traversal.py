# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderHelper(self, root, res):
        if not root:
            return
        
        self.postorderHelper(root.left, res)
        self.postorderHelper(root.right, res)
        res.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorderHelper(root, res)
        return res
        