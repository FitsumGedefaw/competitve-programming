class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivotNum = nums[0]
        
        greaterNums, equalNums, smallerNums = [], [], []
        
        for num in nums:
            if num < pivotNum:
                smallerNums.append(num)
            elif num > pivotNum:
                greaterNums.append(num)
            else:
                equalNums.append(num)
        
        if k <= len(greaterNums):
            return self.findKthLargest(greaterNums, k)
        
        elif k > len(greaterNums) + len(equalNums):
            return self.findKthLargest(smallerNums, k - (len(greaterNums) + len(equalNums)))
        
        else:
            return equalNums[0]
        