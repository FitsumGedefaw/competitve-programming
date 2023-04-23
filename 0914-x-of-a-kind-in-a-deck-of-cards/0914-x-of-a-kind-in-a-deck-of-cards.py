class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool: 
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        cts = Counter(deck).values()
        
        commonGCD = reduce(gcd, cts)
            
        return commonGCD > 1
            
        