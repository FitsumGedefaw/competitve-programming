# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findModeHelper(self, currNode, freq):
        if not currNode:
            return 
        
        freq[currNode.val] = freq.get(currNode.val, 0) + 1
        self.findModeHelper(currNode.left, freq)
        self.findModeHelper(currNode.right, freq)
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        self.findModeHelper(root, freq)
        
        maxFreq = max(freq.values())
        
        return [nodeVal for nodeVal in freq if freq[nodeVal] == maxFreq]
        
        