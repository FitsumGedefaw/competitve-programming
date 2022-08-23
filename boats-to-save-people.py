class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        numOfBoats = 0
        while left <= right:
            if left == right:
                numOfBoats += 1
                break
            else:
                if people[left] + people[right] > limit:
                    right -= 1
                    numOfBoats += 1
                else:
                    left += 1
                    right -= 1
                    numOfBoats += 1
        return numOfBoats
                    
