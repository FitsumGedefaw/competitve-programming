class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = -1
        freq = {}
        winlen = maxFreq = 0
        
        while r < len(s):
            if winlen - maxFreq <= k:
                r += 1
                if r < len(s):
                    winlen += 1
                    freq[s[r]] = freq.get(s[r], 0) + 1
                    maxFreq = max(maxFreq, freq[s[r]])
                    
            else:
                winlen -= 1
                freq[s[l]] -= 1
                l += 1
                
        return winlen
                                
                
        
        