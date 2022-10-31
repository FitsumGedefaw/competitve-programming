class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        st = deque()
        for d in directions:
            if st and st[-1]=="R" and d=="L":
                ans += 2
                st.pop()
                while st and st[-1] == "R":
                    ans += 1
                    st.pop()
                st.append("S")
            elif st and st[-1]=="S" and d=="L":
                ans += 1
            elif st and st[-1]=="R" and d=="S":
                ans += 1
                st.pop()
                while st and st[-1] == "R":
                    ans += 1
                    st.pop()
                st.append("S")
            else:
                st.append(d)
        return ans
                
                
                
                