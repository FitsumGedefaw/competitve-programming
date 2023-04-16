# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node, ans):
            ans.append("(" + str(node.val))
            
            if node.left and not node.right:
                dfs(node.left, ans)
            
            elif not node.left and node.right:
                ans.append("()")
                dfs(node.right, ans)
            
            elif node.left and node.right:
                dfs(node.left, ans)
                dfs(node.right, ans)
                
            ans.append(")")
            return
        
        
                    
        ans = []
        dfs(root, ans)
        ans = "".join(ans)
        
        return ans[1: len(ans)-1]
        
        
        
        
        
        