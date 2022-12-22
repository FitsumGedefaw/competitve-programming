class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters_in_s = {}
        
        for letter in s:
            letters_in_s[letter] = letters_in_s.get(letter, 0) + 1
        
        for letter in t:
            if letter in letters_in_s:
                letters_in_s[letter] -= 1
                
                if letters_in_s[letter] == 0:
                    letters_in_s.pop(letter)
                    
            else:
                return letter
            
                    
        