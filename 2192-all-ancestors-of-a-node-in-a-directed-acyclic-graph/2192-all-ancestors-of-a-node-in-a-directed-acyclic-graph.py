class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = [0] * (n)
        
        for src, dst in edges:
            graph[src].append(dst)
            incoming[dst] += 1
                        
        ans = [set() for _ in range(n)]
        queue = deque([node for node in range(n) if incoming[node] == 0])
        
        while queue:
            node = queue.popleft()
            
            for neigh in graph[node]:
                for ansc in ans[node]:
                    ans[neigh].add(ansc)
                ans[neigh].add(node)
                incoming[neigh] -= 1
                
                if incoming[neigh] == 0:
                    queue.append(neigh)
                    
        for i in range(n):
            ans[i] = sorted(ans[i])
        return ans
                    
        
                
        
        
        
        