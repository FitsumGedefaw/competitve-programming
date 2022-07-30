import math
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
       result = 0
       numsCounter = Counter(nums)
       for x in numsCounter:
            if x == k/2:
                if numsCounter[x] >= 2:
                    result += math.floor(numsCounter[x]/2)
                    numsCounter[x] = 0
            
            elif numsCounter[k-x]:
                result += min(numsCounter[x], numsCounter[k-x])
                numsCounter[x] = 0
                numsCounter[k-x] = 0
       return result
