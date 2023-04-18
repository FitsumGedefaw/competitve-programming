# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node, path):
            path.append(str(node.val))
            
            if not node.left and not node.right:
                ans.append(deepcopy(path))
                path.pop()
                return 
            
            if not node.right:
                dfs(node.left, path)
            elif not node.left:
                dfs(node.right, path)
            else:
                dfs(node.left, path)
                dfs(node.right, path)
                
            path.pop()
            
        dfs(root, [])
        res = 0
        for num in ans:
            res += (int("".join(num)))
        
        return res
        
        
            
            
        
        