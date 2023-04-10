class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        numOfSubArrs = 0
        left = right = 0

        while right < len(nums):
            if nums[right] % k == 0:
                i = right
                while i >= left and gcd(nums[i], nums[right]) != k:
                    i -= 1
                
                numOfSubArrs += (i - left + 1)
            
            else:
                left = right + 1
            
            right += 1
        
        return numOfSubArrs
            
                
            