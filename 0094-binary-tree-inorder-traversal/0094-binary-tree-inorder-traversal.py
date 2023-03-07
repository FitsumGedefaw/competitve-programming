# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseInorder(self, root, res):
        if root == None:
            return
        
        self.traverseInorder(root.left, res)
        res.append(root.val)
        self.traverseInorder(root.right, res)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverseInorder(root, res)
        return res

        