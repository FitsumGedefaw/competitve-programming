class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = ""
        st = deque()
        inSt = set()
        lastOcc = {}
        for i, c in enumerate(s):
            lastOcc[c] = i
        for i in range(len(s)):
            if s[i] not in inSt:
                while st and s[i] < st[-1] and lastOcc[st[-1]] > i:
                    inSt.remove(st.pop())  
                st.append(s[i])
                inSt.add(s[i])
        while st:
            ans += st.popleft()
        return ans
                
            
                
        