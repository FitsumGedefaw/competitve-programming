class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValidWC(capacity):
            daysTaken = 0
            temp = capacity
            
            for weight in weights:
                if weight > temp:
                    daysTaken += 1
                    temp = capacity-weight
                
                else:
                    temp -= weight
            daysTaken += 1
            
            return daysTaken <= days
        
        totalSum = maxWeight = 0
        for weight in weights:
            totalSum += weight
            maxWeight = max(maxWeight, weight)
        
        low, high = maxWeight, totalSum
        while low < high:
            mid = low+(high-low)//2
            
            if isValidWC(mid):
                high = mid
            else:
                low = mid+1
        
        return low
        
        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        