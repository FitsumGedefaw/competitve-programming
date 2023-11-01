class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i, v in enumerate(nums):
            if (target-v) in comp:
                return [comp[target-v], i]
            comp[v] = i


