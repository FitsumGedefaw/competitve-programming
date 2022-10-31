class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = []
        for i in range(len(position)):
            ft = (target - position[i])/speed[i]
            temp.append([position[i], ft])
        temp.sort()
        st = deque()
        for i in range(len(temp)-1, -1, -1):
            if st and temp[i][1] <= st[-1][1]:
                continue
            st.append(temp[i])
        return len(st)