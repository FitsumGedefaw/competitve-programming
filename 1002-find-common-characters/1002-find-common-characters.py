class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commonCharacters = []
        
        charsInWords = []
        
        for word in words:
            charsInWords.append(Counter(word))
            
        firstWordChars = charsInWords[0]
        
        for char in firstWordChars:
            minCount = firstWordChars[char]
            
            for i in range(1, len(charsInWords)):
                wordChars = charsInWords[i]
                
                if char in wordChars:
                    minCount = min(minCount, wordChars[char])
                else:
                    minCount = 0
                    break
            if minCount > 0:
                for i in range(minCount):
                    commonCharacters.append(char)
                    
        return commonCharacters
                
                
            
        