class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index2 = 0
        for i in range(1, len(nums)):
            if nums[i] != 0 and nums[i-1] == 0:
                index2 = i
                while index2 and nums[index2 - 1] == 0:
                    index2 -= 1
                nums[index2], nums[i] = nums[i], 0
        
                
            
