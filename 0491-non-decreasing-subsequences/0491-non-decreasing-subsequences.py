class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seq = []
        
        def backtrack(idx):
            if idx == len(nums):
                if len(seq) >= 2:
                    res.add(tuple(seq))
                return
            
            if not seq or seq[-1] <= nums[idx]:
                seq.append(nums[idx])
                backtrack(idx + 1)
                seq.pop()
                
            backtrack(idx + 1)
            
        backtrack(0)
        return res
                
        
        