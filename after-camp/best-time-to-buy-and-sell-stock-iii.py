class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def findMaxProfit(idx, remTransactions, bought):
            if idx >= len(prices) or remTransactions == 0:
                return 0
            
            if (idx+1, remTransactions, bought) not in memo:
                memo[(idx+1, remTransactions, bought)] = findMaxProfit(idx+1, remTransactions, bought)

            profit = memo[(idx+1, remTransactions, bought)] #profit by skipping this stock
            
            if bought:
                #profit by selling this stock, you can only sell in this case
                if (idx+1, remTransactions - 1, False) not in memo:
                    memo[(idx+1, remTransactions - 1, False)] = findMaxProfit(idx+1, remTransactions - 1, False)
                profit = max(profit, memo[(idx+1, remTransactions - 1, False)] + prices[idx])
            else:
                #prfit by buying this stock
                if (idx+1, remTransactions, True) not in memo:
                    memo[(idx+1, remTransactions, True)] = findMaxProfit(idx+1, remTransactions, True)
                profit = max(profit, memo[(idx+1, remTransactions, True)] - prices[idx])
            
            return profit

        return findMaxProfit(0, 2, False)
            

            
        