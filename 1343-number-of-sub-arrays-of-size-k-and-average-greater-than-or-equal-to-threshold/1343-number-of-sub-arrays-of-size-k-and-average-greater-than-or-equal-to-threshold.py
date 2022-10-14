class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        ans = 0
        l, r = 0, k-1
        while r < len(arr):
            windowSum = arr[r] if l==0 else arr[r]-arr[l-1]
            if windowSum/k >= threshold:
                ans += 1
            l, r = l+1, r+1
        return ans
            