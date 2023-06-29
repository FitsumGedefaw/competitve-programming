class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [0] * n
        
        for i in range(n):
            arr[i] = start + 2 * i
            
        res = arr[0]
        
        for i in range(1, n):
            res = res ^ arr[i]
            
        return res
        