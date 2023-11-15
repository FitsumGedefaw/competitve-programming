class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        minDiff = float('inf')
        for i in range(len(timePoints)):
             if i + 1 < len(timePoints):
                 time1 = (int(timePoints[i][ : 2]) * 60) + int(timePoints[i][3 : ])
                 time2 = (int(timePoints[i+1][ : 2]) * 60) + int(timePoints[i+1][3 : ])
                 ShortestDiff = min(time2 - time1, 1440 - time2 + time1)
                 minDiff = min(minDiff, ShortestDiff)

        if len(timePoints) > 1:
            time1 = (int(timePoints[0][ : 2]) * 60) + int(timePoints[0][3 : ])
            time2 = (int(timePoints[-1][ : 2]) * 60) + int(timePoints[-1][3 : ])
            minDiff = min(minDiff, 1440 - time2 + time1)

        return minDiff
                

        