class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        heapify(piles)
        
        while k:
            rem = -1 * heappop(piles)
            rem -= math.floor(rem / 2)
            heappush(piles, -1*rem)
            k -= 1
            
        return sum(-1 * val for val in piles)
            
        
    