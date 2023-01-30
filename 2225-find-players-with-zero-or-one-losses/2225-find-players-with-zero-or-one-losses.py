class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
                
        for winner, loser in matches:
            winners[winner] = winners.get(winner, 0) + 1
            losers[loser] = losers.get(loser, 0) + 1
            
        notLostAnyMatches = [w for w in winners if w not in losers]
        notLostAnyMatches.sort()
        
        lostOneMatch = [l for l in losers if losers[l] == 1]        
        lostOneMatch.sort()
        
        return [notLostAnyMatches, lostOneMatch]
        