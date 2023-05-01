class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        minimumTime = 0
        tree = defaultdict(list)
        visited = set()
        
        for node1, node2 in edges:
            tree[node1].append(node2)
            tree[node2].append(node1)
        
        def doesAppleExist(node):
            nonlocal minimumTime
            
            visited.add(node)
            appleExist = False
            
            for child in tree[node]:
                if child not in visited and doesAppleExist(child):
                    minimumTime += 2
                    appleExist = True
                    
            return appleExist or hasApple[node]
        
        doesAppleExist(0)
        
        return minimumTime
                    