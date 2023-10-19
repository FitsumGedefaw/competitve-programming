class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency = {i:[] for i in range(n)}
        for u, v, w in flights:
            adjacency[u].append((v, w))

        def dijkstra(src, dst, k):
            minHeap = [(0, 0, src)]
            while minHeap:
                cost, stops, city = heapq.heappop(minHeap)
                visited[city] = stops
                if city ==dst:
                    return cost
                if stops > k:
                    continue
                for next_city, next_cost in adjacency[city]:
                    if next_city not in visited or visited[next_city] > stops:
                        heapq.heappush(minHeap, [cost + next_cost, stops + 1, next_city])
            return -1

        visited = {}
        return dijkstra(src, dst, k)