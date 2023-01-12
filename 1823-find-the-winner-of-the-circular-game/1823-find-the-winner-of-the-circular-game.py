class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        
        start, end = 0, k-1
        
        while len(arr) > 1:
            arr.pop(end)
            start = end % len(arr)
            end = (start + k - 1) % len(arr)
            
        return arr[0]