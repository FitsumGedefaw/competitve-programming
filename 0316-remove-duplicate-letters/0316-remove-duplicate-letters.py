class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res = ""
        st = deque()
        d = {}
        visited = set()
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in s:
            d[c] -= 1
            if c not in visited:
                while st and d[st[-1]] > 0 and c < st[-1]:
                    visited.remove(st.pop())
                st.append(c)
                visited.add(c)
        while st:
            res += st.popleft()
        return res
                
            
                
        