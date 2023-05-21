class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = [(i, 10 ** 4, 1) for i in range(n+1)]
        def findRep(node):
            repre, minP, size = rep[node]
            if node == repre:
                return (node, minP, size)
            
            rep[node] = findRep(repre)
            return rep[node]
        
        def union(node1, node2, roadLen):
            node1Rep, minP1, size1  = findRep(node1)
            node2Rep, minP2, size2 = findRep(node2)
            
            if size1 <= size2:
                rep[node2Rep] = (node2Rep, min(minP1, minP2, roadLen), size1 + size2)
                rep[node1Rep] = rep[node2Rep]   
            else:
                rep[node1Rep] = (node1Rep, min(minP1, minP2, roadLen), size1 + size2)
                rep[node2Rep] = rep[node1Rep]
                
        def connected(node1, node2):
            return findRep(node1)[0] == findRep(node2)[0]
                
        for node1, node2, roadLen in roads:
            union(node1, node2, roadLen)
        
        return findRep(1)[1]