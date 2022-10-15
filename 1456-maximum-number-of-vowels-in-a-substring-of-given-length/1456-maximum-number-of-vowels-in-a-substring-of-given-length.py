class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        temp = [0]*len(s)
        for i in range(len(s)):
            if s[i] in ["a","e","i","o","u"]:
                temp[i] = 1
        for i in range(1,len(temp)):
            temp[i] += temp[i-1]
        l, r = 0, k-1
        while r < len(temp):
            windowSum = temp[r] if l==0 else temp[r]-temp[l-1]
            ans = max(ans, windowSum)
            l, r = l+1, r+1
        return ans