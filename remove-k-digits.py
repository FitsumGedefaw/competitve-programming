class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        else:
            ans = ""
            mon_stack = deque()
            for i in range(len(num)):
                while k > 0 and mon_stack and mon_stack[-1] > num[i]:
                    mon_stack.pop()
                    k -= 1
                mon_stack.append(num[i])
            while len(mon_stack) > k:
                ans += mon_stack.popleft()
            while len(ans) >= 2 and ans[0] == "0":
                ans = ans[1 : ]
            return ans
                
