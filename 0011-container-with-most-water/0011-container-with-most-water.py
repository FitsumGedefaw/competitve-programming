class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        
        maxAmount = 0
        
        while l < r:
            amount = (r-l) * min(height[l], height[r])
            
            maxAmount = max(maxAmount, amount)
            
            if height[r] <= height[l]:
                r -= 1
                
            else:
                l += 1
                
        return maxAmount
            
        