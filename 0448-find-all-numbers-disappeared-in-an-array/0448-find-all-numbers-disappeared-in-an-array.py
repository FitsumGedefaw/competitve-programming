class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        
        while i < len(nums):
            corrPos = nums[i] - 1
            
            if i == corrPos or nums[i] == nums[corrPos]:
                i += 1
            else:
                nums[i], nums[corrPos] = nums[corrPos], nums[i]
                
        return [i+1 for i in range(len(nums)) if i != nums[i]-1]        
            
        