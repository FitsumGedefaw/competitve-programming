class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        #for n in nums:
        #    count[n] += 1
            
        res = 0
        
        for i in nums:
            if count[i] > 1:
                res += count[i] - 1
                count[i] -= 1
        return res