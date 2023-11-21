class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        if nums[0] <= nums[1]:
            i = 1
            while i + 1 < len(nums) and nums[i] <= nums[i+1]:
                i += 1
            if i == len(nums) - 1:
                return True
        
        i = 0
        while i + 1 < len(nums) and nums[i] >= nums[i+1]:
            i += 1
        return i == len(nums) - 1


        