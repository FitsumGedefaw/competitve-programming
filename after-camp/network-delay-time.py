class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, weight in times:
            graph[src].append((weight, dst))
        dists = [float('inf') for _ in range(n + 1)]
        dists[k] = 0
        minHeap = [(0, k)]
        visited = set()

        while minHeap:
            distFromSource, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            for w, neigh in graph[node]:
                neighdistFromSource = distFromSource + w
                if neighdistFromSource < dists[neigh]:
                    dists[neigh] = neighdistFromSource
                    heapq.heappush(minHeap, (neighdistFromSource, neigh))
        
        minTimes = [dists[i] for i in range(1, n+1) if i != k and dists[i] != float('inf')]
        if len(minTimes) == 0 or len(minTimes) < n-1:
            print(dists)
            return -1 
        else:
            return max(minTimes)





        