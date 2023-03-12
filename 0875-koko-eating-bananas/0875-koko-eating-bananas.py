class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValidSpeed(k):
            hoursTaken = 0
            
            for numOfBananas in piles:
                if numOfBananas % k == 0:
                    hoursTaken += numOfBananas // k
                else:
                    hoursTaken += (numOfBananas//k)+1
            
            return hoursTaken <= h
        
        low, high = 1, max(piles)
        while low < high:
            mid = (low+high)//2
            
            if isValidSpeed(mid):
                high = mid
            else:
                low = mid+1
                
        return low
                
        
            
                    
                
                
        