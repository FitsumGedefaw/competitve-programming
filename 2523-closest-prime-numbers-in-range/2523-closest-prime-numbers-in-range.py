class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(x: int) -> bool:
            if x == 1:
                return False
            d = 2
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 1
            return True
        
        primes = []
        
        for num in range(left, right + 1):
            if isPrime(num):
                if primes and num <= primes[-1] + 2:
                    return [primes[-1], num]
                primes.append(num)
        
        if len(primes) < 2:
            return [-1, -1]
        
        minGap = float('inf')
        ans = []
        
        for i in range(len(primes)-1, 0, -1):
            gap = primes[i] - primes[i - 1]
            if gap <= minGap:
                ans = [primes[i-1], primes[i]]
            
        return ans
                

        