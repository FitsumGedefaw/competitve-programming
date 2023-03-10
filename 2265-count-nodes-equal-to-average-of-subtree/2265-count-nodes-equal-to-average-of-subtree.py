# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ASHelper(self, currNode, ans):
        #print("ans: ", ans)
        if not currNode:
            return [0, 0]
        
        leftSubTree = self.ASHelper(currNode.left, ans)
        rightSubTree = self.ASHelper(currNode.right, ans)
        wholeSubTree = [leftSubTree[0]+rightSubTree[0]+currNode.val, leftSubTree[1]+ rightSubTree[1] + 1]
        
        if (wholeSubTree[0] // wholeSubTree[1]) == currNode.val:
            ans[0] += 1
        
        return wholeSubTree
        
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.ASHelper(root, ans)
        
        return ans[0]
        
        
        
        
        
        

        
        
        