class Solution:
    def makeGood(self, s: str) -> str:
        res = ""
        st = deque()
        for c in s:
            if c.islower():
                if st and st[-1] == c.upper():
                    st.pop()
                else:
                    st.append(c)
            elif c.isupper():
                if st and st[-1] == c.lower():
                    st.pop()
                else:
                    st.append(c)
        while st:
            res += st.popleft()
        return res

        