# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrderHelper(self, root, res):
        if not root:
            return
        
        res.append(root.val)
        self.preOrderHelper(root.left, res)
        self.preOrderHelper(root.right, res)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preOrderHelper(root, res)
        return res