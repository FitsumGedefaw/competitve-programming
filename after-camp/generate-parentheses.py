class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def check(parStr):
            stack = []
            for ch in parStr:
                if ch == "(":
                    stack.append(ch)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

        ans = []

        def dfs(pos, candidate):
            if pos == (2 * n) + 1:
                if check(candidate):
                    ans.append(candidate)
                return
            
            dfs(pos + 1, candidate + "(")
            dfs(pos + 1, candidate + ")")

        dfs(1, "")
        return ans



        

        