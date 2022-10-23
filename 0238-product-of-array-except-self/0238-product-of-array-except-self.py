class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        res[0] = 1
        temp = 1
        for i in range(1, len(nums)):
            temp *= nums[i-1]
            res[i] = temp
        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp *= nums[i+1]
            res[i] = res[i] * temp
        return res
            
            
            