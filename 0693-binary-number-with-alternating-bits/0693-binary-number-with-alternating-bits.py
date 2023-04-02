class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def isEven(num):
            return True if num % 2 == 0 else False
        
        while n:
            if isEven(n) == isEven(n >> 1):
                return False
            n = n >> 1
        
        return True
                
        