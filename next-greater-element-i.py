class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tempHash = {v : i for i,v in enumerate(nums1)}
        ans = [-1]*len(nums1)
        mStack = deque()
        for num in nums2:
            while mStack and num > mStack[-1]:
                val = mStack.pop()
                ans[tempHash[val]] = num
            if num in tempHash:
                mStack.append(num)
                
        return ans
