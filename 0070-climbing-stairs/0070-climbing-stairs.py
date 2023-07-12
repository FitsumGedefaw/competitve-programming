class Solution:
    def climbStairs(self, n: int) -> int:
        numOfWays = [1, 1]
        i = n - 2
        
        while i > -1:
            temp = numOfWays[0]
            numOfWays[0] = numOfWays[0] + numOfWays[1]
            numOfWays[1] = temp
            i -= 1
            
        return numOfWays[0]
            
        
            
            
        
        
        