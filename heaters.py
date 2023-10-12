class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def findClosestHeater(target):
            if target <= heaters[0]:
                return heaters[0] - target
            elif target > heaters[-1]:
                return target - heaters[-1]
            
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = left + (right - left) // 2
                if target == heaters[mid]:
                    return 0
                elif target < heaters[mid]:
                    if target >= heaters[mid-1]:
                        return min(heaters[mid] - target, target - heaters[mid-1])
                    right = mid - 1
                else:
                    if target <= heaters[mid+1]:
                        return min(target - heaters[mid], heaters[mid+1] - target)
                    left = mid+1

        heaters.sort()
        maxClosestDist = 0
        for house in houses:
            maxClosestDist = max(maxClosestDist, findClosestHeater(house))
        return maxClosestDist