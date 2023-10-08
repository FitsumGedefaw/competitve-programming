class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # construct adjlist 
        adjlist = {}
        for u,v,w in times:
            if u in adjlist:
                adjlist[u].append([v, w])
            else:
                adjlist[u] = [[v, w]]

        

        parent = [None] * (n + 1)
        distance = [float('inf')] * (n + 1)
        parent[0] = k
        parent[k] = k
        distance[0] = 0
        distance[k] = 0
        piority_queue = [(0, k)]

        while piority_queue:
            node_distance, node = heapq.heappop(piority_queue)

            # get the neighbours
            
            if node not in adjlist:
                continue
            for nbrnode, nbrweight in adjlist[node]:
                newdistance = nbrweight + node_distance

                if newdistance < distance[nbrnode]:
                    heapq.heappush(piority_queue, (newdistance,nbrnode ))
                    distance[nbrnode] = newdistance
                    parent[nbrnode] = node
        
        if None in parent:
            return -1
        
        return max(distance)