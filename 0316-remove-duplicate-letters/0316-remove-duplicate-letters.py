class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        numOfOcc = {}
        for ch in s:
            numOfOcc[ch] = numOfOcc.get(ch, 0) + 1
            
        st = []
        inSt = set()
        
        for ch in s:
            if ch not in inSt:
                while st and st[-1] > ch and numOfOcc[st[-1]] > 1:
                    print(numOfOcc)
                    c = st.pop()
                    inSt.remove(c)
                    numOfOcc[c] -= 1
                    
                st.append(ch)
                inSt.add(ch)
            else:
                numOfOcc[ch] -= 1
                
        return "".join(st)
                    
                
            
        