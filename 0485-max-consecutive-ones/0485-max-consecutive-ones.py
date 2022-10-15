class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = r = maxlen = 0
        while r < len(nums):
            if nums[r] == 0:
                l = r+1
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen