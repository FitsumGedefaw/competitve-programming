# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res += "None "
            else:
                res += str(node.val) + " "
                queue.append(node.left)
                queue.append(node.right)
        
        return res.strip()
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        treeData = deque(data.split())
        #print(treeData)
        rootVal = treeData.popleft()
        if rootVal == "None":
            return None
        root = TreeNode(int(rootVal))
        queue = deque([root]) #queue of nodes with no child yet

        while queue:
            curr = queue.popleft()
            if treeData:
                leftChildVal = treeData.popleft()
                if leftChildVal != "None":
                    curr.left = TreeNode(int(leftChildVal))
                    queue.append(curr.left)
                rightChildVal = treeData.popleft()
                if rightChildVal != "None":
                    curr.right = TreeNode(int(rightChildVal))
                    queue.append(curr.right)
        
        return root
                


                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))