class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        l = r = ct = 0
        while r < len(nums):
            if nums[r]==0:
                ct += 1
            if ct > k:
                while l < len(nums) and nums[l] != 0:
                    l += 1
                l, ct = l+1, ct-1 
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen
            
                