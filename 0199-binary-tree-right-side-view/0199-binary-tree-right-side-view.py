# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rsvHelper(self, currParents, res):
        if not currParents:
            return
        
        for i in range(len(currParents)-1, -1, -1):
            if currParents[i].right:
                res.append(currParents[i].right.val)
                break
            if currParents[i].left:
                res.append(currParents[i].left.val)
                break
        
        nextParents = []
        for parent in currParents:
            if parent.left:
                nextParents.append(parent.left)
            if parent.right:
                nextParents.append(parent.right)
        
        self.rsvHelper(nextParents, res)
            
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = [root.val]
        self.rsvHelper([root], res)
        return res
        
        