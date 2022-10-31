class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = deque()
        i = j = 0
        while j < len(popped):
            if st and st[-1] == popped[j]:
                st.pop()
                j += 1
            else:
                if i < len(pushed):
                    st.append(pushed[i])
                    i += 1
                else:
                    return False
        return True
                    
            
                