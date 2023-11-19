class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        numOfGoodPairs = 0
        
        for num in count:
            n = count[num]
            
            numOfGoodPairs += (n * (n-1)//2)
            
        return numOfGoodPairs
            