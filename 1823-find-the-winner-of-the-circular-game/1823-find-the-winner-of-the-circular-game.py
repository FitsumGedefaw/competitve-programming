class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        
        i, j = 0, k-1
        
        while len(arr) > 1:
            arr.pop(j)
            i = j % len(arr)
            j = (i + k - 1) % len(arr)
            
        return arr[0]