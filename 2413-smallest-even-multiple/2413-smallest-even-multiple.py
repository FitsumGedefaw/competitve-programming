class Solution:
    def smallestEvenMultiple(self, n: int) -> int: 
        for i in range(n,300):
            if i%2==0 and i%n==0:
                return i
                break