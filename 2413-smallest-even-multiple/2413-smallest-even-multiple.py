class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num = n
        
        while num < 300:
            if num % n == 0 and num % 2 == 0:
                return num
            
            num += 1 