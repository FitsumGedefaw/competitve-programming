class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        existingNums = {num for num in nums}
        
        #missingNum = -1
        
        for num in range(0, len(nums)+1):
            if num not in existingNums:
                return num
                
        
            
        