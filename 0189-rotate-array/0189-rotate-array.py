class Solution:
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    
    def reverse(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        self.reverse(0, len(nums)-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len(nums)-1, nums)
        
        
        
        
        