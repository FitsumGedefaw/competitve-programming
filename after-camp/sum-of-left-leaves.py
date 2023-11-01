# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ans):
            if node .left:
                if not node.left.left and not node.left.right:
                    ans[0] += node.left.val
                else:
                    dfs(node.left, ans)
            
            if node.right:
                dfs(node.right,ans)
        
        ans = [0]
        dfs(root, ans)
        return ans[0]
        