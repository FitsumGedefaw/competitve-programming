class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        #T.C: O(n)
        #S.C: O(1) 26 letters
        
        res = []
        
        lastOcc = {}
        
        for idx,ch in enumerate(s):
            lastOcc[ch] = idx
        
        partitionStartIdx = partitionEndIdx = 0
        
        for i in range(len(s)):
            if lastOcc[s[i]] > partitionEndIdx:
                partitionEndIdx = lastOcc[s[i]]
                
            if i == partitionEndIdx:
                res.append(partitionEndIdx - partitionStartIdx + 1)
                partitionStartIdx = i+1
                
        return res
                
           
        
                
                
        
        