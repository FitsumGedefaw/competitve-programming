# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        
        def preorder(node, currPath, currSum):
            if not node: return
            nonlocal res
            currSum += node.val
            temp = currSum
            
            if currSum == targetSum: res += 1
                
            for num in currPath:
                temp -= num
                if temp == targetSum: res += 1
            
            currPath.append(node.val)
            preorder(node.left, currPath, currSum)
            preorder(node.right, currPath, currSum)
            currPath.pop()
        
        preorder(root, [], 0)
        return res
                
        