# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def findSumOfGChildren(node):
            res = 0
            if node.left:
                res += (node.left.left.val if node.left.left else 0)
                res += (node.left.right.val if node.left.right else 0)
            if node.right:
                res += (node.right.left.val if node.right.left else 0)
                res += (node.right.right.val if node.right.right else 0)
            return res
        
        totSum = [0]
        
        def dfs(node):
            if not node:
                return
            if node.val % 2 == 0:
                totSum[0] += findSumOfGChildren(node)
                
            dfs(node.left)
            dfs(node.right)
         
        dfs(root)
        return totSum[0]
        