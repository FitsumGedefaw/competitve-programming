class Solution:
    def similarPairs(self, words: List[str]) -> int:
        w = []
        
        for word in words:
            w.append(set(word))
        
        ct = 0
        
        for i in range(len(w)):
            for j in range(i):
                
                if w[j] == w[i]:
                    ct += 1
                    
        return ct
        
            
        