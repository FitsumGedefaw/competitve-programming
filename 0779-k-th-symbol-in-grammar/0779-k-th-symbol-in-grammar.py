class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        prevStrLen = (2 ** (n-1)) / 2
        
        if k <= prevStrLen:
            return self.kthGrammar(n-1, k)
        
        else:
            prevK = k % prevStrLen if k % prevStrLen != 0 else prevStrLen
            
            res = self.kthGrammar(n-1, prevK)
            return 0 if res == 1 else 1
            