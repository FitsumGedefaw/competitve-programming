class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        incomings = defaultdict(list)
        
        for i in range(len(graph)):
            for dest in graph[i]:
                incomings[dest].append(i)
      
        outgoing = [len(dests) for dests in graph]
        safeNodes = []
        queue = deque()
        
        for node in range(len(outgoing)):
            if outgoing[node] == 0:
                queue.append(node)
                safeNodes.append(node)
        
        while queue:
            node = queue.popleft()
            
            for neigh in incomings[node]:
                outgoing[neigh] -= 1
                
                if outgoing[neigh] == 0 or (outgoing[neigh] == 1 and neigh == node):
                    queue.append(neigh)
                    safeNodes.append(neigh)
                    
        safeNodes.sort()
        return safeNodes
        
        
        
        
            
        
        