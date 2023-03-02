class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        
        val1 = self.myPow(x, n//2)
        
        if n % 2 == 0:
            val2 = val1
        else:
            val2 = x * val1
                
        
        return val1 * val2
        