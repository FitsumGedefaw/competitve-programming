class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [cost[-2], cost[-1]]
        
        for i in range(len(cost)-3, -1, -1):
            temp = minCost[0]
            minCost = [cost[i] + min(minCost), temp]
        
        return min(minCost)
        
        