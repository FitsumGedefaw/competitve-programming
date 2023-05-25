class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        currMin = nums[0]
        currMed = float('inf')
        
        for num in nums:
            if num < currMin:
                currMin = num
            
            elif currMin < num < currMed:
                currMed = num
            
            elif num > currMed:
                return True
        
        return False
        
        
        