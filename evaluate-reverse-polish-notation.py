class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for x in tokens:
            if x == "+":
                top = stack.pop()
                belowTop = stack.pop()
                stack.append(belowTop + top)
            elif x == "-":
                top = stack.pop()
                belowTop = stack.pop()
                stack.append(belowTop - top)
            elif x == "*":
                top = stack.pop()
                belowTop = stack.pop()
                stack.append(belowTop * top)
            elif x == "/":
                top = stack.pop()
                belowTop = stack.pop()
                if (belowTop * top) < 0 and (belowTop % top) != 0:
                    stack.append((belowTop // top)+1)
                else:
                    stack.append(belowTop // top)
            else:
                stack.append(int(x))
        return stack.pop()
                
