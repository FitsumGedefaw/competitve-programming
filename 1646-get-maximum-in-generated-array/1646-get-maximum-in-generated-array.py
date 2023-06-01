class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        arr = [0] * (n+1)
        arr[1] = 1
        maxVal = float('-inf')
        
        for i in range(n+1):
            if i % 2 == 0:
                arr[i] = arr[i // 2]
                
            else:
                idx = (i - 1) // 2
                arr[i] = arr[idx] + arr[idx+1]
                maxVal = max(maxVal, arr[i])
                
        
        return maxVal
        
        