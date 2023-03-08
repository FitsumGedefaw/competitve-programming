# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def extract(self, node, row, col, res):
        if not node:
            return

        res.append([col, row, node.val])
        self.extract(node.left, row+1, col-1, res)
        self.extract(node.right, row+1, col+1, res)

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.extract(root, 0, 0, res)
        res.sort()
        
        new_res = []
        right = 0
        while right < len(res):
            temp = [res[right]]
            while right < len(res)-1 and res[right][0] == res[right+1][0]:
                temp.append(res[right+1])
                right += 1
            right += 1
            new_res.append(temp)

        ans = []
        for i in new_res:
            temp = []
            for c, r, val in i:
                temp.append(val)

            ans.append(temp)
        
        return ans