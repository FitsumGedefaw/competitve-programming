class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_sPair = []
        for i in range(0, len(position)):
            p_sPair.append([position[i] , speed[i]])
        p_sPair.sort()
        stack = deque()
        for i in range (len(p_sPair) - 1, -1, -1):
            p,s = p_sPair[i]
            finishTime = (target - p)/s
            if stack and finishTime <= stack[-1]:
                continue
            else:
                stack.append(finishTime)
        return len(stack)    
        
        
