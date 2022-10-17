class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        l1, r1 = 0, firstLen-1
        ans = 0
        while r1 < len(nums):
            l2, r2 = r1+1, r1+secondLen
            temp = 0
            while r2 < len(nums):
                temp = max(temp, nums[r2]-nums[l2-1])
                l2, r2 = l2+1, r2+1
            if l1 >= secondLen:
                l2, r2 = 0, secondLen-1
                while r2 < l1:
                    temp = max(temp, nums[r2]-nums[l2-1] if l2>0 else nums[r2])
                    l2, r2 = l2+1, r2+1
            windowSum = nums[r1] if l1 == 0 else nums[r1]-nums[l1-1]
            ans = max(ans, windowSum+temp)
            l1, r1 = l1+1, r1+1
        return ans
            