class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0
        
        for _amount in range(1, len(minCoins)):
            for coin in coins:
                if _amount - coin >= 0:
                    minCoins[_amount] = min(minCoins[_amount], 1 + minCoins[_amount - coin])
                
        
        return minCoins[amount] if minCoins[amount] != amount+1 else -1
        