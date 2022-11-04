class Solution:
    def calculate(self, s: str) -> int:
        currentNum, preOp, s, st = 0, '+', s + '+', deque()
        for c in s:
            if c.isdigit():
                currentNum = currentNum*10 + int(c)
            elif c == ' ':
                continue
            else:
                if preOp == '+':
                    st.append(currentNum)
                elif preOp == '-':
                    st.append(-currentNum)
                elif preOp == '*':
                    st.append(st.pop() * currentNum)
                elif preOp == '/':
                    st.append(math.trunc(st.pop()/currentNum))
                currentNum, preOp = 0, c
        res = 0
        while st:
            res += st.popleft()
        return res
                
       
