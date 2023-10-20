class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(s[0], 1)]

        for i in range(1, len(s)):
            if stack and s[i] == stack[-1][0]:
                if stack[-1][1] == k-1:
                    count = k-1
                    while count > 0:
                        stack.pop()
                        count -= 1
                else:
                    stack.append((s[i], stack[-1][1] + 1))
            else:
                stack.append((s[i], 1))
        
        ans = ""
        for ch, ct in stack:
            ans += ch
        return ans