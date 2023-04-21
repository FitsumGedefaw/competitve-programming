# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _maxPathSum = [-1000]
        
        def findMaxPathSum(node):
            if not node:
                return -1000
            
            leftMaxPathSum = findMaxPathSum(node.left)
            rightMaxPathSum = findMaxPathSum(node.right)
            
            _maxPathSum[0] = max(_maxPathSum[0], leftMaxPathSum + node.val + rightMaxPathSum)
            
            totMax = max(leftMaxPathSum, rightMaxPathSum)
            maxFromNode = totMax + node.val if totMax > 0 else node.val
            
            _maxPathSum[0] = max(_maxPathSum[0], maxFromNode)
            return maxFromNode
        
        findMaxPathSum(root)
        return _maxPathSum[0]
            
        