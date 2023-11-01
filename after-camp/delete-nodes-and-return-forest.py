# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = [root]
      #  print("root:", root)

        def deleteNode(curr, targetVal, targetPar):
            if curr:
                if curr.val == targetVal:
                    #print(curr, targetVal)
                    if curr.left:
                        forest.append(curr.left)
                    if curr.right:
                        forest.append(curr.right)
                    if not targetPar:
                        forest.remove(curr)
                    else:
                        #print(curr.val)
                        if targetPar.left and curr.val == targetPar.left.val:
                            targetPar.left = None
                        else:
                            targetPar.right = None
                    return True
                deleteNode(curr.left, targetVal, curr)
                deleteNode(curr.right, targetVal, curr)
                return False

        for node in to_delete:
            for currRoot in forest:
                if deleteNode(currRoot, node, None):
                    break

        return forest

