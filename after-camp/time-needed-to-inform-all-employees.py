class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ans = 0
        subs = defaultdict(list)
        for emp, man in enumerate(manager):
            subs[man].append(emp)
        informed = deque([(headID, 0)])
        while informed:
            nextLevel = []
            while informed:
                man, timeTaken = informed.popleft()
                ans = max(ans, timeTaken + informTime[man])
                for sub in subs[man]:
                    nextLevel.append((sub, timeTaken + informTime[man]))
            informed = deque(nextLevel)
        return ans

                
        