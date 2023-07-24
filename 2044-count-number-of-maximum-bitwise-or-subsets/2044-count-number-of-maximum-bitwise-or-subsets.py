class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = 0
        
        def arrOR(arr):
            res = 0
            for num in arr:
                res |= num
            return res
        
        maxOr = arrOR(nums)
        
        def backtrack(subset, i):
            nonlocal ans
            if i == len(nums):
                if arrOR(subset) == maxOr:
                    ans += 1
                return
            
            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()
            backtrack(subset, i + 1)
            
        backtrack([], 0)
        return ans