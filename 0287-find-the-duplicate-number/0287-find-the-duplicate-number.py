class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            corrPos = nums[i] - 1
            
            if i != corrPos:
                if nums[i] == nums[corrPos]:
                    return nums[i]
                nums[i], nums[corrPos] = nums[corrPos], nums[i]
                
            else:
                i += 1
        
        
        