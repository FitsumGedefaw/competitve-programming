from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        arr = SortedList()

        def findMinDiff(val):
            left, right = 0, len(arr) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2

                if arr[mid] <= val:
                    left = mid
                else:
                    right = mid
            return min(abs(val - arr[left]), abs(arr[right] - val))

        ans = float('inf')
        for i in range(x, len(nums)):
            arr.add(nums[i - x])
            ans = min(ans, findMinDiff(nums[i]))
        return ans
        

        