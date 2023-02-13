class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        maxNumofMatches = 0
        
        players.sort()
        trainers.sort()
        
        i = j = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                maxNumofMatches += 1
                i, j = i+1, j+1
                
            else:
                j += 1
                
        return maxNumofMatches
        