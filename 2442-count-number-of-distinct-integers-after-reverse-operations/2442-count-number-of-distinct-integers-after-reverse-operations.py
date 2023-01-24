class Solution:
    def reverseInt(self, num):
        numStr = str(num)
        
        temp = [0] * len(numStr)
        
        for j in range(len(numStr)-1, -1, -1):
            temp[len(numStr)-1-j] = numStr[j]
            
        while temp[0] == "0":
            temp.pop(0)
        
        return [numStr, "".join(temp)]
        
        
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinictNums = set()
        
        for num in nums:
            numStr, numStrRev = self.reverseInt(num)
            distinictNums.add(numStr)
            distinictNums.add(numStrRev)
            
        return len(distinictNums)
            
        