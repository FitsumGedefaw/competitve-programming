class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxPairSum = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            pairSum = nums[l] + nums[r]
            if pairSum > maxPairSum:
                maxPairSum = pairSum
            l += 1
            r -= 1
        return maxPairSum
