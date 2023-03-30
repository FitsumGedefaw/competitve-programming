class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x), bin(y)
        i, j = len(x)-1, len(y)-1
        hdist = 0
        
        while i > 1 or j > 1:
            if i > 1 and not j > 1:
                if x[i] == "1":
                    hdist += 1
            
            elif not i > 1 and j > 1:
                if y[j] == "1":
                    hdist += 1
            
            else:
                if x[i] != y[j]:
                    hdist += 1
            
            i, j = i-1, j-1
            
        return hdist
        
            
        
        
        