from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for x in s:
            if x == "(" or x == "{" or x == "[":
                stack.append(x)
            elif stack and x == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and x == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and x == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        
        
