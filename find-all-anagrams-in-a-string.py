class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        ds, dp = {}, {}
        for i in range(len(p)):
            dp[p[i]] = dp.get(p[i], 0) + 1
            ds[s[i]] = ds.get(s[i], 0) + 1
        res = [0] if dp == ds else []
        l = 0
        for r in range(len(p), len(s)):
            ds[s[r]] = ds.get(s[r], 0) + 1
            ds[s[l]] -= 1
            if ds[s[l]] == 0:
                ds.pop(s[l])
            l += 1
            if ds == dp:
                res.append(l)
        return res
