class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for op in logs:
            if op == "../" and ans != 0:
                ans -= 1
            elif op == "../" and ans == 0:
                continue
            elif op == "./":
                continue
            else:
                ans += 1
        return ans
            