class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winners = []
        score = {}
        currWinnerScore = 0
        
        for i in range(len(persons)):
            person, time = persons[i], times[i]
            score[person] = score.get(person, 0) + 1
            
            if score[person] >= currWinnerScore:
                self.winners.append((person, time))
                currWinnerScore = score[person]
        
    def q(self, t: int) -> int:
        low, high = 0, len(self.winners)-1
        
        if self.winners[-1][1] <= t:
            return self.winners[-1][0]
            
        while low < high:
            mid = (low+high)//2
            
            if self.winners[mid][1] > t:
                high = mid
            else:
                low = mid + 1
            
        return self.winners[low-1][0] 
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)