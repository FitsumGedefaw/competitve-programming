class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        _targetIndices = []
        
        nums.sort()
        
        i = 0
        while i < len(nums) and nums[i] != target:
            i += 1
        
        while i < len(nums) and nums[i] == target:
            _targetIndices.append(i)
            i += 1
            
        return _targetIndices
    
    
        
        
        
        