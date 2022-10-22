class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = deque()
        res = list(prices)
        for i,v in enumerate(prices):
            while st and v <= prices[st[-1]]:
                j = st.pop()
                res[j] = prices[j] - v
            st.append(i)
        return res
        