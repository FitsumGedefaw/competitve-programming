class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = basket = ""
        st = deque()
        for i in range(len(S)):
            if S[i] == "(":
                st.append(S[i])
            else:
                st.pop()
            basket += S[i]
            if len(st) == 0:
                res += basket[1: -1]
                basket = ""
        return res