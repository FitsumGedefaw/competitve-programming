class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psum = 0
        d = defaultdict(int)
        d[0] = 1
        ans = 0
        for i in range(len(nums)):
            psum += nums[i]
            if (psum-goal) in d:
                ans += d[psum-goal]
            d[psum] += 1
        return ans