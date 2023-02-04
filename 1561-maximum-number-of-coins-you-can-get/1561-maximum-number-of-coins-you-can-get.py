class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        maxNumOfCoins = 0
        
        numOfTurns = len(piles) / 3
        
        piles.sort()
        
        i = len(piles)-2
        
        while numOfTurns > 0:
            maxNumOfCoins += piles[i]
            
            i -= 2
            numOfTurns -= 1
            
        return maxNumOfCoins
            
        
        