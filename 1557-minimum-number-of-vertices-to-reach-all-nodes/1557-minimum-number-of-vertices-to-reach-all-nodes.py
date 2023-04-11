class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nonReachables = []
        reachables = defaultdict(list)
        
        for source, destination in edges:
            reachables[destination].append(source)
            
        for i in range(n):
            if i not in reachables:
                nonReachables.append(i)
                
        return nonReachables
                
        
            
        
        