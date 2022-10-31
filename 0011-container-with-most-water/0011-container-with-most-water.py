class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = 0
        l, r = 0, len(height)-1
        while l < r:
            if height[l] <= height[r]:
                a = height[l] * (r-l)
                ma = max(ma, a)
                l += 1
            else:
                a = height[r] * (r-l)
                ma = max(ma, a)
                r -= 1
        return ma
                
            
        