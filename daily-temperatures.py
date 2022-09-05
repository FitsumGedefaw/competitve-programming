class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        m_stack = deque()
        for i in range(len(temperatures)):
            while m_stack and temperatures[i] > m_stack[-1][1]:
                ind , val = m_stack.pop()
                answer[ind] = i - ind
            m_stack.append([i, temperatures[i]])
        return answer
