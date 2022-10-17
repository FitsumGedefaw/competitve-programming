class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        minlen = len(nums)
        windowSum = 0
        while r < len(nums):
            windowSum += nums[r]
            while windowSum >= target:
                minlen = min(minlen, r-l+1)
                l, windowSum = l+1, windowSum - nums[l]
            r += 1
        if minlen == len(nums):
            totalSum = 0
            for num in nums:
                totalSum += num
            if totalSum < target:
                return 0
        return minlen
            
            