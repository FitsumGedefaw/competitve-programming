class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        incoming = [[i, 0, i] for i in range(n)] 
        outgoing = defaultdict(list)
        
        for a, b in richer:
            outgoing[a].append(b)
            incoming[b][1] += 1
        
        queue = deque([p for p in incoming if p[1] == 0])
        res = [0 for _ in range(n)]
        
        while queue:
            person, inc, minQ = queue.popleft()
            res[person] = minQ
            
            for neigh in outgoing[person]:
                incoming[neigh][2] = minQ if quiet[minQ] < quiet[incoming[neigh][2]] else incoming[neigh][2]
                incoming[neigh][1] -= 1
                
                if incoming[neigh][1] == 0:
                    queue.append(incoming[neigh])
                    
        return res
                
                