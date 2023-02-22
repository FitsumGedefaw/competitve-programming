class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = float('-inf')
        
        l = r = 0
        
        _sum = 0
        while r < k:
            _sum += nums[r]
            r += 1
            
        maxSum = max(maxSum, _sum)
            
        while r < len(nums):
            _sum = _sum + nums[r] - nums[l]
            maxSum = max(maxSum, _sum)
            l, r = l+1, r+1
            
        return maxSum/k
        