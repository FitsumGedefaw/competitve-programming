class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ans = ""
        lastOcc = {}
        for i, v in enumerate(s):
            lastOcc[v] = i
        st = deque()
        inSt = set()
        for i in range(len(s)):
            if s[i] not in inSt:
                while st and st[-1] > s[i] and lastOcc[st[-1]] > i:
                    inSt.remove(st.pop())
                st.append(s[i])
                inSt.add(s[i])
        while st:
            ans += st.popleft()
        return ans
            
                
                
                