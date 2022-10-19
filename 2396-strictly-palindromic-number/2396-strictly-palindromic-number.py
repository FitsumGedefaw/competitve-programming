class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def fun1(self, n, b):
            res = ""
            q= n
            while q > 0:
                res = str(q%b) + res
                q = q / b
            return res
        for i in range(2, n-1):
            temp = fun1(self,n, i)
            l, r = 0, len(temp)-1
            while l < r:
                if temp[l] != temp[r]:
                    return False
                l, r = l+1, r-1
        return True
            