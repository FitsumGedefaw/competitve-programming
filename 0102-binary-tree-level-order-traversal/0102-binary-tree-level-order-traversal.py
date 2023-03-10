# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traversal(self, node, level, store):
        if not node:
            return
        
        store[level].append(node.val)
        self.traversal(node.left, level+1, store)
        self.traversal(node.right, level+1, store)
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)
        self.traversal(root, 0, store)
        return store.values()        
        
        