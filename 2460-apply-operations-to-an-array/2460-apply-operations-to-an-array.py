class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i], nums[i+1] = nums[i]*2, 0
                
        resArray = [0] * len(nums)
        
        p = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                resArray[p] = nums[i]
                p += 1
        
        return resArray
