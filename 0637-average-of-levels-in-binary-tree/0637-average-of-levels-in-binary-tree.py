# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        queue = deque([root])
        
        while queue:
            levelSum = 0
            levelLen, k = len(queue), 0
            
            while k < levelLen:
                node = queue.popleft()
                levelSum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                k += 1
            
            averages.append(levelSum / levelLen)
        
        return averages            
        
        