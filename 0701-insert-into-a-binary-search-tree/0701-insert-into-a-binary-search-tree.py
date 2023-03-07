# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def insertHelper(self, root, val):
#         # if root == None:
#         #     root = ListNode(val)
#         #     return
            
#         if val < root.val:
#             if root.left == None:
#                 root.left = TreeNode(val)
#                 return
#             else:
#                 self.insertHelper(root.left, val)
        
#         else:
#             if root.right == None:
#                 root.right = TreeNode(val)
#                 return
#             else:
#                 self.insertHelper(root.right, val)
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
            
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root
        
        # return curr