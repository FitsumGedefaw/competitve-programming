class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        maxlen = 0
        l = r = 0
        while r  < len(fruits):
            d[fruits[r]] = r
            if len(d) > 2:
                minI = min(d.values())
                l = minI + 1
                del d[fruits[minI]]
            maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen
                
