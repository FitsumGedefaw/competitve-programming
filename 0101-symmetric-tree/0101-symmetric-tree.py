# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        st = [[root.left, root.right]]
        
        while st:
            root1, root2 = st.pop()
            
            if not root1 and not root2:
                continue
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            
            st.append([root1.left, root2.right])
            st.append([root1.right, root2.left])
        
        return True
        