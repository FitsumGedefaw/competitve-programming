class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(node, visited):
            if node in visited:
                return 0
            
            visited.add(node)
            ans = 0

            for neigh in graph[node]:
                ans += dfs(neigh, visited)

            return 1 + ans
            
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            affected = []
            for j in range(len(bombs)):
                if j != i:
                    x2, y2, r2  = bombs[j]
                    dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                    if dist <= r1:
                        affected.append(j)
            graph[i] = affected
        
        maxNumOfBombs = 0
        visited = set()
        
        for node in graph:
            maxNumOfBombs = max(maxNumOfBombs, dfs(node, visited))
            visited = set()
        
        return maxNumOfBombs
        
        
                        
                    
        
        