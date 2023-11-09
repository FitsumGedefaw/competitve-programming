class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        prevSmallestMin = [0] * len(nums)
        
        minSofar = float('inf')
        for i in range(len(prevSmallestMin)):
            prevSmallestMin[i] = minSofar
            minSofar = min(minSofar, nums[i])
            
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] < nums[i]:
                thirdNum = stack.pop()
                
                if thirdNum > prevSmallestMin[i]:
                    return True
                
            stack.append(nums[i])
            
        
                
        
        