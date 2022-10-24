class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = deque()
        res = temp = ""
        nlb = nrb = 0
        for i in range(len(s)):
            if s[i] == "(":
                nlb += 1
                st.append(s[i])
            else:
                nrb += 1
                if nlb == nrb:
                    while len(st) > 1:
                        temp = st.pop() + temp
                    st.pop()
                    res, temp, nlb, nrb = res+temp, "", 0, 0
                else:
                    st.append(s[i])
        return res
                    