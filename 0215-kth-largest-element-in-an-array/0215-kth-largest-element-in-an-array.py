class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivotNum = nums[0]
        
        greaterNums = [num for num in nums if num > pivotNum]
        equalNums = [num for num in nums if num == pivotNum]
        smallerNums = [num for num in nums if num < pivotNum]
        
        if k <= len(greaterNums):
            return self.findKthLargest(greaterNums, k)
        
        elif k > len(greaterNums) + len(equalNums):
            return self.findKthLargest(smallerNums, k - (len(greaterNums) + len(equalNums)))
        
        else:
            return equalNums[0]
        