class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedLetters = []
        
        N = max(len(word1), len(word2))
        
        for i in range(N):
            if i < len(word1):
                mergedLetters.append(word1[i])
                
            if i < len(word2):
                mergedLetters.append(word2[i])
            
        return "".join(mergedLetters)
        
        
        