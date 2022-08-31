class Solution:
    def maxArea(self, height: List[int]) -> int:
        windowArea = maxArea = 0
        left , right = 0 , len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                windowArea = (right - left) * height[left]
                maxArea = max(maxArea, windowArea)
                left += 1
            else:
                windowArea = (right - left) * height[right]
                maxArea = max(maxArea, windowArea)
                right -= 1
        return maxArea
