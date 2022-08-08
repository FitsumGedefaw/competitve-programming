class Solution:
    def reverseParentheses(self, s: str) -> str:
        result = ""
        stack = deque()
        for char in s:
            if char != ")":
                stack.append(char)
            else:
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                for x in temp:
                    stack.append(x)
        while len(stack) != 0:
            result += stack.popleft()
        return result    
