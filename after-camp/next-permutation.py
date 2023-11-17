class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        while right > 0 and nums[right] <= nums[right - 1]:
            right -= 1

        if right == 0:
            nums.reverse()
        else:
            pos, val = right - 1, nums[right - 1]
            minValIdx = pos + 1
            for right in range(len(nums) - 1, pos, -1):
                if nums[right] > val and nums[right] < nums[minValIdx]:
                    minValIdx = right
            
            nums[pos], nums[minValIdx] = nums[minValIdx], nums[pos]

            i = pos + 1
            for val in sorted(nums[pos + 1 : ]):
                nums[i] = val
                i += 1

        

            
        