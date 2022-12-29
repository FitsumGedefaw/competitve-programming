class Solution:
    def areInOrder(self, d, word1, word2):
        for i in range(min(len(word1), len(word2))):
            if d[word1[i]] < d[word2[i]]:
                return True
            elif d[word1[i]] > d[word2[i]]:
                return False
            else: 
                if i == len(word2)-1 and i < len(word1)-1:
                    return False
                elif i == len(word1)-1:
                    return True
                else:
                    continue  
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = {}
        
        for index, ch in enumerate(order):
            alphabet[ch] = index
            
        for i in range(len(words)-1):
            isCorrectOrder = self.areInOrder(alphabet, words[i], words[i+1])
            
            if isCorrectOrder:
                continue
            else:
                return False
        return True
        
        