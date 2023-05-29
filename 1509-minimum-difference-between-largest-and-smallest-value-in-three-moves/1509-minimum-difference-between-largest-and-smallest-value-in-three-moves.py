class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) > 3:
            nums.sort()
            w = len(nums) - 4
            ans = float('inf')
            
            for i in range(len(nums)):
                if w + i >= len(nums):
                    break
                    
                ans = min(ans, nums[i+w] - nums[i])
                
            
            return ans
        
        return 0
                
                
        