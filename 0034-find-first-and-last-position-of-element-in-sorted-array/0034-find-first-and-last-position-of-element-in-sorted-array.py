class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        start = bisect_left(nums, target)
        end = bisect_right(nums, target)
        
        ans.append(start if (start < len(nums) and nums[start] == target) else -1)
        ans.append(end-1 if (nums and nums[end-1] == target) else -1)
        
        return ans
        