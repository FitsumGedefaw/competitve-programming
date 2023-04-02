class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def wordToBin(word):
            res = 0
            letterBins = [1 << (ord(letter) - ord("a")) for letter in word]
            
            for lettBin in letterBins:
                res = res | lettBin
            
            return res
        
        wordBins = [wordToBin(word) for word in words]
        maxProduct = 0
        
        for i in range(len(wordBins)):
            for j in range(i+1, len(wordBins)):
                if wordBins[i] & wordBins[j] == 0:
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
                    
        
        return maxProduct
        
        
            
        

        