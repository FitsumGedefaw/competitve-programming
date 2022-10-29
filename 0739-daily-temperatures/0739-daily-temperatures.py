class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = deque()
        for i, v in enumerate(temperatures):
            while st and st[-1][1] < v:
                ans[st[-1][0]] = i - st[-1][0]
                st.pop()
            st.append([i,v])
        return ans