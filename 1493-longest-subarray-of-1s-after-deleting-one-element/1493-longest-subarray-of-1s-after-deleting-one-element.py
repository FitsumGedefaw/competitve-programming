class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = maxlen = 0
        k = 1
        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            while k < 0 and l <= r:
                if nums[l] == 0:
                    k += 1
                l += 1
            maxlen = max(maxlen, r-l)
            r += 1
        return maxlen