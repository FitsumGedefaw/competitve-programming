class Solution:
    def interpret(self, command: str) -> str:
        correspondingLetters = []
        i = 0
        
        while i < len(command):
            if command[i] == "G":
                correspondingLetters.append("G")
                i += 1
            
            else: 
                if command[i+1] == ")":
                    correspondingLetters.append("o")
                    i += 2
                    
                else:
                    correspondingLetters.append("al")
                    i += 4
        
        return "".join(correspondingLetters)
                    
                
        
        
        
        