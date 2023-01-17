class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totalWealthes = [sum(accs) for accs in accounts]
        
        return max(totalWealthes)