class UnionFind:
    def __init__(self, n):
        self.rep = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        
    def findRep(self, node):
        if node != self.rep[node]:
            self.rep[node] = self.findRep(self.rep[node])
        return self.rep[node]
    
    def union(self, node1, node2):
        node1Rep = self.findRep(node1)
        node2Rep = self.findRep(node2)
        
        if self.size[node1Rep] < self.size[node2Rep]:
            self.rep[node1Rep] = node2Rep
            self.size[node2Rep] += self.size[node1Rep]
        else:
            self.rep[node2Rep] = node1Rep
            self.size[node1Rep] += self.size[node2Rep]
            
    def connected(self, node1, node2):
        return self.findRep(node1) == self.findRep(node2)
        
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        merged = defaultdict(list)
        
        for idx1, idx2 in pairs:
            uf.union(idx1, idx2)
         
        for i in range(len(s)):
            merged[uf.findRep(i)].append(s[i])
        
        for rep in merged:
            merged[rep].sort(reverse=True)
        
        temp = [merged[uf.findRep(i)].pop() for i in range(len(s))]
        return "".join(temp)
        
        