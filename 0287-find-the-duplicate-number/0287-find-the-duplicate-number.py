class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicateNum = -1
        left, right = 1, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            numsLessThanOrEqualToMid = 0
            for num in nums:
                if num <= mid: 
                    numsLessThanOrEqualToMid += 1
            
            if numsLessThanOrEqualToMid > mid:
                duplicateNum = mid
                right = mid - 1
            else:
               left = mid + 1
        
        return duplicateNum