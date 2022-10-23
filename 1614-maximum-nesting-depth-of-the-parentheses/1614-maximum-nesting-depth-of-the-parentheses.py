class Solution:
    def maxDepth(self, s: str) -> int:
        ans = temp = 0
        for i in range(len(s)):
            if s[i] == "(":
                temp += 1
                ans = max(ans, temp)
            elif s[i] == ")":
                temp -= 1
        return ans