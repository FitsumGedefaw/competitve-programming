class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        nexGreaIdx = {}
        
        for idx, val in enumerate(temperatures):
            while st and temperatures[st[-1]] < val:
                nexGreaIdx[st.pop()] = idx
                
            st.append(idx)
               
        for i in range(len(temperatures)):
            temperatures[i] = nexGreaIdx[i] - i if i in nexGreaIdx else 0
        
        return temperatures
        