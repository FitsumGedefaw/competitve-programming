class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = deque()
        res = list(prices)
        for i in range(len(prices)):
            while st and prices[i] <= prices[st[-1]]:
                j = st.pop()
                res[j] = prices[j] - prices[i]
            st.append(i)
        return res
        