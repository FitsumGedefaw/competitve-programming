class Solution:
    def reverseInt(self, num):
        numStr = str(num)
        
        return int(numStr[::-1])
        
        
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinictNums = set()
        
        for num in nums:
            distinictNums.add(num)
            distinictNums.add(self.reverseInt(num))
            
        return len(distinictNums)
            
        