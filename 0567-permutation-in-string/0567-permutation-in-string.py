class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Chars = {}
        for ch in s1:
            s1Chars[ch] = s1Chars.get(ch, 0) + 1

        substrInS2 = {}
        l = r = 0
        
        while r < len(s1):
            substrInS2[s2[r]] = substrInS2.get(s2[r], 0) + 1
            r += 1
            
        if substrInS2 == s1Chars:
            return True
        
        while r < len(s2):
            substrInS2[s2[r]] = substrInS2.get(s2[r], 0) + 1
            substrInS2[s2[l]] -= 1
            
            if substrInS2[s2[l]] == 0:
                del substrInS2[s2[l]]
            
            if substrInS2 == s1Chars:
                return True
            l, r = l+1, r+1
            
        return False
            
            
        
            
        
        