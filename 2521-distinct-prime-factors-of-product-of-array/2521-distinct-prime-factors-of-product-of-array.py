class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def trial_division_simple(n):
            factorization = set()
            d = 2

            while d * d <= n:
                while n % d == 0:
                    factorization.add(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.add(n)

            return factorization
        
        res = set()
        for num in nums:
            res = res.union(trial_division_simple(num))
            
        return len(res)

            
        