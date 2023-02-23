class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        _sum = 0
        
        for i in range(len(nums)):
            _sum += nums[i]
            nums[i] = _sum
            
        return nums