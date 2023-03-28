class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
        return [num for num in range(1, n+1) if num not in nums]
        