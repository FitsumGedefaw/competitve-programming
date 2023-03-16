class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def res(divisor):
            totalSum = 0
            for num in nums:
                totalSum += math.ceil(num/divisor)
            
            return totalSum
        
        low, high = 1, max(nums)
        
        while low < high:
            mid = low + (high-low)//2
            
            if res(mid) <= threshold:
                high = mid
            else:
                low = mid + 1
        
        return low
            
        
        