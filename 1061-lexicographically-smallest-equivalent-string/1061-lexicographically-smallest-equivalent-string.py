class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        chars = "abcdefghijklmnopqrstuvwxyz"
        rep = {ch: (ch, ch, 1) for ch in chars}
        
        def findRep(node):
            repre, minCh, size = rep[node]
            if node == repre:
                return (node, minCh, size)
            
            rep[node] = findRep(repre)
            return rep[node]
        
        def union(node1, node2):
            node1Rep, minCh1, size1  = findRep(node1)
            node2Rep, minCh2, size2 = findRep(node2)
            
            if size1 <= size2:
                rep[node2Rep] = (node2Rep, min(minCh1, minCh2), size1 + size2)
                rep[node1Rep] = rep[node2Rep]                
            else:
                rep[node1Rep] = (node1Rep, min(minCh1, minCh2), size1 + size2)
                rep[node2Rep] = rep[node1Rep]
                
        def connected(node1, node2):
            return findRep(node1)[0] == findRep(node2)[0]
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        temp = [findRep(ch)[1] for ch in baseStr]
        return "".join(temp)
        