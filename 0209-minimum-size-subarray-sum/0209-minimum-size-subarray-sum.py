class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        winSum = 0
        
        l = 0
        r = -1
        
        while r < len(nums):
            if winSum >= target:
                minlen = min(minlen, r-l+1 )
                winSum -= nums[l]
                l += 1
                
            else:
                r += 1
                if r < len(nums):
                    winSum += nums[r]
                    
        return minlen if minlen != float('inf') else 0
        