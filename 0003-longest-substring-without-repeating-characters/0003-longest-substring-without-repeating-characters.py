class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        maxlen = 0
        
        l = r = 0
        
        while r < len(s):
            if s[r] in visited:
                while s[l] != s[r]:
                    visited.remove(s[l])
                    l += 1
                l += 1
                
            maxlen = max(maxlen, r-l+1)
            
            visited.add(s[r])
            r += 1
            
        return maxlen
        
        
                