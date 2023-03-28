class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingNum = -1
        nums.append(-1)
        
        i = 0
        while i < len(nums):
            while nums[i] != -1 and i != nums[i]:
                val = nums[i]
                nums[i], nums[val] = nums[val], val
            
            if nums[i] == -1:
                missingNum = i
            
            i += 1
            
        return missingNum
        
        
            
            
        
        
                    
             
            
        