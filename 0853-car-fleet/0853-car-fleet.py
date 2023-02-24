class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        finishTime = []
        for i in range(len(position)):
            ft = (target-position[i])/speed[i]
            finishTime.append([position[i], ft])
            
        finishTime.sort()
        
        st = []
        for i in range(len(finishTime)-1, -1, -1):
            if st and st[-1][1] >= finishTime[i][1]:
                continue
            
            st.append(finishTime[i])
            
        return len(st)
            
        