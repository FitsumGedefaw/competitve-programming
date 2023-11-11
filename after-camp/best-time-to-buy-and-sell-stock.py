class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minCost = prices[0]

        for i in range(1, len(prices)):
            if prices[i] >= minCost:
                ans = max(ans, prices[i] - minCost)
            else:
                minCost = prices[i]

        return ans
                
                
        