class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        PSA = [nums[0]]
        for i in range(1, len(nums)):
            PSA.append(PSA[i-1] + nums[i])
        if PSA[-1] - PSA[0] == 0:
            return 0
        else:
            for i in range(1, len(PSA) - 1):
                if PSA[i-1] == PSA[-1] - PSA[i]:
                    return i
        if PSA[-2] == 0:
            return len(nums) - 1
        else: 
            return -1
