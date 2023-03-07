# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            else:
                temp = root.right #Find the deepest left to the right child of the node to be deleted
                while(temp.left): # which is the minimum node  in the right subtree
                    temp = temp.left
                
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        
        return root
        
        