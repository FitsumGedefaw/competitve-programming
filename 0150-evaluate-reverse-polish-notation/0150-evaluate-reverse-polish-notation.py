class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = deque()
        for c in tokens:
            if c not in "+-*/":
                st.append(int(c))
            else:
                if c == '+':
                    st.append(st.pop() + st.pop())
                elif c == '-':
                    temp = st.pop()
                    st.append(st.pop() - temp)
                elif c == '*':
                    st.append(st.pop() * st.pop())
                elif c == '/':
                    temp = st.pop()
                    st.append(math.trunc(st.pop()/temp))
        return st.pop()
                
