class UnionFind:
    def __init__(self) -> None:
        self.rep = {}
        #self.size = defaultdict(int)

    def findRep(self, node):
        if node not in self.rep:
            self.rep[node] = node
            return node
        if node == self.rep[node]:
            return node
        self.rep[node] = self.findRep(self.rep[node])
        return self.rep[node]
        
    def union(self, node1, node2):
        node1Rep = self.findRep(node1)
        node2Rep = self.findRep(node2)
        self.rep[node2Rep] = node1Rep

        #if size[node1Rep] <= size[node2Rep]:
         #   rep[node1Rep] = node2Rep
          #  size[node2Rep] += size[node1Rep]

#        else:
 #           rep[node2Rep] = node1Rep
  #          size[node1Rep] += size[node2Rep]

    def connected(self, node1, node2):
        return self.findRep(node1) == self.findRep(node2)
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind()
        for idx, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                uf.union(idx, acc[j])
        
        merged = defaultdict(list)
        for node in uf.rep:
            if type(node) == str:
                merged[uf.findRep(node)].append(node)
        
        return [[accounts[idx][0], *sorted(merged[idx])] for idx in merged]
        
        
        