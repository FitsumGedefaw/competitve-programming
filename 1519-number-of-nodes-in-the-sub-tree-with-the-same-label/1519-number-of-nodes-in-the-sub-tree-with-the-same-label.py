class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        
        for node1, node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        
        counts = defaultdict(int)
        ans = [0] * n
        
        def dfs(node, parent):
            labelCounts = defaultdict(int)
            labelCounts[labels[node]] = 1
            
            for child in tree[node]:
                if child == parent:
                    continue
                childLabelCts = dfs(child, node)
                for label in childLabelCts:
                    labelCounts[label] += childLabelCts[label]
            
            ans[node] = labelCounts[labels[node]]
            return labelCounts
        
        dfs(0,-1)
        return ans
                