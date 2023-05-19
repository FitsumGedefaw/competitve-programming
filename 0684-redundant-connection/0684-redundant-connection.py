class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
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
                
        def connected(node1, node2):
            return findRep(node1) == findRep(node2)
        
        for node1, node2 in edges:
            if connected(node1, node2):
                return [node1, node2]
            
            union(node1, node2)
        
        