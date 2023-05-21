class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rep = [i for i in range(n+1)]
        size = [1 for i in range(n+1)]
        
        def findRep(node):
            if node == rep[node]:
                return node
            
            rep[node] = findRep(rep[node])
            return rep[node]
        
        def union(node1, node2):
            node1Rep = findRep(node1)
            node2Rep = findRep(node2)
            
            if size[node1Rep] <= size[node2Rep]:
                rep[node1Rep] = node2Rep
                size[node2Rep] += size[node1Rep]
                
            else:
                rep[node2Rep] = node1Rep
                size[node1Rep] += size[node2Rep]
        
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)
        
        return n - len([i for i in range(n) if i == findRep(i)])
                
        
        