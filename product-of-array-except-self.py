class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pref = 1
        for i in range(len(nums)):
            ans.append(pref)
            pref *= nums[i]
        postf = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * postf
            postf *= nums[i]
        return ans
