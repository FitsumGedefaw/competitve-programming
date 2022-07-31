class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count = 0
        l = 0
        r = len(piles) - 1
        while l < r:
            count += piles[r-1]
            r -= 2
            l += 1
        return count
