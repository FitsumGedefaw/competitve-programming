class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missingNum = dupNum = -1
        
        i = 0
        while i < len(nums):
            corrPos = nums[i] - 1
            
            if i == corrPos:
                i += 1
            
            elif nums[i] == nums[corrPos]:
                dupNum = nums[i]
                missingNum = i + 1
                i += 1
            
            else:
                nums[i], nums[corrPos] = nums[corrPos], nums[i]
                
        return [dupNum, missingNum]
                
        
        
        