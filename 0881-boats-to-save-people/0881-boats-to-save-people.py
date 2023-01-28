class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        numOfBoats = 0
        
        people.sort()
        
        l, r = 0, len(people)-1
        
        while l <= r:
            if people[l] + people[r] <= limit:
                numOfBoats += 1
                l, r = l+1, r-1
                
            else:
                numOfBoats += 1
                r -= 1
                
        return numOfBoats
                
            
            