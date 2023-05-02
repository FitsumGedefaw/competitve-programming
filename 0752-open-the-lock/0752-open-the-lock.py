class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        
        visited = set(deadends)
        if "0000" in visited:
            return -1
        visited.add("0000")
        
        nextNum = {str(i): [str( (i-1) % 10 ), str( (i+1) % 10 )] for i in range(10)}
        queue = deque([("0000", 0)])
        
        while queue:
            state, depth = queue.popleft()
            
            if state == target:
                return depth
            
            for i in range(4):
                for nextDigit in nextNum[state[i]]:
                    nextState = state[0: i] + nextDigit + state[i+1: ]

                    if nextState not in visited:
                        queue.append((nextState, depth+1))
                        visited.add(nextState)
        
        return -1
                
        