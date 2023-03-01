class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = psum = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(nums)):
            psum += nums[i]
            ans += d[psum - k]
            d[psum] += 1
        return ans
        