# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseInorder(self, currNode, visitedVals):
        if not currNode:
            return
        
        self.traverseInorder(currNode.left, visitedVals)
        visitedVals.append(currNode.val)
        self.traverseInorder(currNode.right, visitedVals)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.traverseInorder(root, res)
        return res[k-1]
        