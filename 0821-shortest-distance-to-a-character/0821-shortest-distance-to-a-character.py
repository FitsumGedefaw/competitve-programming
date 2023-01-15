class Solution:
    def clothestIndex(self, ind, arr):
        minDist = float('inf')
        
        for i in range(len(arr)):
            dist = abs(ind - arr[i])
              
            minDist = min(minDist, dist)
        return minDist
                   
    def shortestToChar(self, s: str, c: str) -> List[int]:
        occIndices = []
        
        for i in range(len(s)):
            if s[i] == c:
                occIndices.append(i)
        res =[]
                       
        for i in range(len(s)):
            if s[i] == c:
                res.append(0)
            else:
                res.append(self.clothestIndex(i, occIndices))
                
        return res
            
                       
                       
                      
                       
                       
        