class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        temp = []
        for idx, interval in enumerate(intervals):
            start, end = interval
            temp.append([start, end, idx])
        
        temp.sort()
        
        for i in range(len(intervals)):
            if intervals[i][1] > temp[-1][0]:
                intervals[i] = -1
            else:
                low, high = 0, len(temp)-1
                
                while low < high:
                    mid = (low + high) // 2
                    
                    if intervals[i][1] <= temp[mid][0]:
                        high = mid
                    else:
                        low = mid + 1
                
                intervals[i] = temp[low][-1]
        
        return intervals
                
        
        