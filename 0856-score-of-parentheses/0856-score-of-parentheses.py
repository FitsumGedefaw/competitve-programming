class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                deepestScore = stack.pop()
                stack[-1] += max(1, 2 * deepestScore)
            
        return stack[0]
        
         
        