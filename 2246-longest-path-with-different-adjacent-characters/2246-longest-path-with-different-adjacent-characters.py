class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        maxLen = [0]
        
        for idx, val in enumerate(parent):
            tree[val].append(idx)
        
        def findMaxLen(node):
            lenAndLabel = [1, s[node]]
            validPathLens = []
            
            for child in tree[node]:
                branchLen = findMaxLen(child)
                if branchLen[1] != s[node]:
                    validPathLens.append(branchLen)
                    
            if len(validPathLens) > 0:
                validPathLens.sort()
                if len(validPathLens) > 1:
                    maxLen[0] = max(maxLen[0],   1 + validPathLens[-1][0] + validPathLens[-2][0])
                lenAndLabel[0] += validPathLens[-1][0]
             
            maxLen[0] = max(maxLen[0], lenAndLabel[0])
            return lenAndLabel
        
        findMaxLen(0)
        return maxLen[0]
        
        
                