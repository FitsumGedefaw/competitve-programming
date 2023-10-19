# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        parents = [[root, 0]]
        maxWidth = 1
        
        while(True):
            children = []
            for node, idx in parents:
                if node.left:
                    children.append([node.left, idx*2])
                
                if node.right:
                    children.append([node.right, 1+idx*2])
                    
            if not children:
                break
                    
            maxWidth = max(maxWidth, children[-1][1] - children[0][1] + 1)
            parents = [i for i in children]
            
        return maxWidth