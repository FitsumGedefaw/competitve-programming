class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        while l < len(nums)-1 and nums[l] != nums[l+1]:
            l += 1
        
        l = l+1
        r = l
                    
        while r < len(nums)-1:
            while r < len(nums)-1 and nums[r] == nums[r+1]:
                r += 1
            
            if r != len(nums)-1:
                r = r+1
                nums[l] = nums[r]
                l += 1
            
        return l