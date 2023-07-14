class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            return min(cost)
        dp = [cost[0],cost[1]] +[0]*(len(cost)-2)
        for i in range(len(cost)-2):
            dp[i+2] = min(dp[i]+cost[i+2],dp[i+1]+cost[i+2])
        return min(dp[-1],dp[-2]) 