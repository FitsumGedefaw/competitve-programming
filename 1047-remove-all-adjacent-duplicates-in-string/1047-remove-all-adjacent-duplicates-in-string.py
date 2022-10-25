class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = ""
        st = deque()
        for i in range(len(s)):
            if st and st[-1] == s[i]:
                st.pop()
            else:
                st.append(s[i])
        while st:
            ans += st.popleft()
        return ans
                
        