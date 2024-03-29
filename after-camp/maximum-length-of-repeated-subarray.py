class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[0 for col in range(m+1)] for row in range(n+1)]
        
        maxlen = 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j] = (dp[i+1][j+1] + 1) if nums1[i] == nums2[j] else 0
                maxlen = max(maxlen, dp[i][j])
        
        return maxlen
        