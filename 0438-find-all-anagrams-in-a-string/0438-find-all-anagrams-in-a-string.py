class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        
        pDict = Counter(p)
        sDict = {}
        
        l = r = 0
        
        while r < len(p):
            sDict[s[r]] = sDict.get(s[r], 0) + 1
            r += 1
          
        if sDict == pDict:
            ans.append(l)
            
        while r < len(s):
            sDict[s[r]] = sDict.get(s[r], 0) + 1
            sDict[s[l]] -= 1
            
            if sDict[s[l]] == 0:
                del sDict[s[l]]
             
            if sDict == pDict:
                ans.append(l+1)
                
            l, r = l+1, r+1
            
        return ans
            


        
        
        