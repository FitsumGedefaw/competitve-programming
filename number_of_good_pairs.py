class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        result = 0
        for x in count:
            n = count[x]
            if n >= 2:
                result += (n*(n - 1)) // 2
        return result
