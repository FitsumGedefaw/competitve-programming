class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums)-1:
            if (i%2) == 0 and nums[i] == nums[i+1]:
                nums.pop(i)
                ans += 1
            else:
                i += 1
        if (len(nums) % 2) != 0:
            ans += 1
        return ans