class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()
        i = 0
        
        while i < len(nums):
            corrPos = nums[i] - 1
            
            if i == corrPos:
                i += 1
            elif nums[i] == nums[corrPos]:
                duplicates.add(nums[i])
                i += 1
            else:
                nums[i], nums[corrPos] = nums[corrPos], nums[i]
            
        return list(duplicates)
                
                
        
        