# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def addParent(node, par):
            if node:
                node.parent = par
                addParent(node.left, node)
                addParent(node.right, node)
        
        addParent(root, None)
        
        queue = deque([(target, 0)])
        visited = set([target])
        
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            
            node, dist = queue.popleft()
            for neigh in (node.parent, node.left, node.right):
                if neigh and neigh not in visited:
                    queue.append((neigh, dist+1))
                    visited.add(neigh)
        
        return []