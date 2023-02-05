class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        
        d = {}
        
        ct = 0
        
        for num in nums_sorted:
            if num not in d:
                d[num] = ct
                
            ct += 1
        
        res = [d[num] for num in nums]
        
        return res
        
                
        
        
        
    
                
                
            