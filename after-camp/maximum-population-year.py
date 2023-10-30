class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0] * 101
        for birthYear, deathYear in logs:
            arr[birthYear-1950] += 1
            arr[deathYear-1950] -= 1
        
        ans = 1950
        prevMax = 0
        prevSum = 0
        for i in range(len(arr)):
            prevSum += arr[i]
            if prevSum > prevMax:
                prevMax = prevSum
                ans = i + 1950

        return ans
                
        