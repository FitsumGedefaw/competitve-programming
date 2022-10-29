class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        ans = ""
        st = deque()
        for i in range(len(num)):
            while st and st[-1] > num[i] and k > 0:
                st.pop()
                k -= 1
            st.append(num[i])
        while len(st) > k:
            ans += st.popleft()
        while len(ans) > 1 and ans[0] == "0":
            ans = ans[1:]
        return ans