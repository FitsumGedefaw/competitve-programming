class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        prevMin = []
        minVal = nums[0]
        
        for i in range(len(nums)):
            minVal = min(minVal, nums[i])
            prevMin.append(minVal)
            
        nextMax = [0] * len(nums)
        maxVal = nums[-1]
        
        for i in range(len(nums)-1, -1, -1):
            maxVal = max(maxVal, nums[i])
            nextMax[i] = maxVal
            
        for i in range(len(nums)):
            if prevMin[i] < nums[i] < nextMax[i]:
                return True
        
        return False
                
            
            
        