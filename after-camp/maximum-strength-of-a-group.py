class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nums.sort()
        maxProd = 1
        i = 0
        F = 0

        while i < len(nums):
            if nums[i] == 0:
                i += 1
            elif nums[i] < 0:
                if i + 1 < len(nums) and nums[i + 1] < 0:
                    F = 1
                    maxProd *= (nums[i] * nums[i + 1])
                    i += 2
                else:
                    i += 1
            else:
                F = 1
                for num in nums[i : ]:
                    maxProd *= num
                break
            
        return maxProd if F == 1 else max(nums)

        