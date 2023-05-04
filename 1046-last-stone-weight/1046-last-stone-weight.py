class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [(-1 * w) for w in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            
            if x != y:
                heapq.heappush(stones, (y + (-1 * x)))
                
        return 0 if len(stones) == 0 else (-1 * stones[0])
        