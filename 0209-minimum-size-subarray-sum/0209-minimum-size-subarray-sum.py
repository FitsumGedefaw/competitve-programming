class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        minlen = float('inf')
        windowSum = 0
        while r < len(nums):
            windowSum += nums[r]
            while windowSum >= target:
                minlen = min(minlen, r-l+1)
                l, windowSum = l+1, windowSum - nums[l]
            r += 1
            
        return minlen if minlen != float('inf') else 0
            
            