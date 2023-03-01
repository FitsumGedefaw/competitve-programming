class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        ans = psum = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(nums)):
            psum += nums[i]
            ans += d[psum - k]
            d[psum] += 1
        return ans
              
	   
                
                
            