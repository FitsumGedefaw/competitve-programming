class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = [i for i in range(n)]
        size = [1 for i in range(n)]
        
        def findRep(node):
            if node == rep[node]:
                return node
            
            rep[node] = findRep(rep[node])
            return rep[node]
        
        def union(x, y):
            xrep = findRep(x)
            yrep = findRep(y)
            
            if xrep != yrep:
                if size[xrep] <= size[yrep]:
                    rep[xrep] = yrep
                    size[yrep] += size[xrep]
                    
                else:
                    rep[yrep] = xrep
                    size[xrep] += size[yrep]
                    
        def connected(x, y):
            return findRep(x) == findRep(y)
        
        for src, dst in edges:
            union(src, dst)
            
        return connected(source, destination)
            
        