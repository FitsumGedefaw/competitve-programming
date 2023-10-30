class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            
            mid = left + (right - left) // 2
            if (target < nums[0] and nums[mid] < nums[0]) or (target >= nums[0] and nums[mid] >= nums[0]):
                competitor = nums[mid]
            elif nums[mid] < nums[0]:
                competitor = float('inf')
            else:
                competitor = float('-inf')

            if competitor < target:
                left = mid + 1
            elif competitor > target:
                right = mid - 1
            else:
                return mid
        
        return -1

        