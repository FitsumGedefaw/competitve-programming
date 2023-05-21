class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        chars = "abcdefghijklmnopqrstuvwxyz"
        rep = {ch: ch for ch in chars}
        size = {ch: 1 for ch in chars}
        
        def findRep(ch):
            if ch == rep[ch]:
                return ch
            
            rep[ch] = findRep(rep[ch])
            return rep[ch]
        
        def union(ch1, ch2):
            ch1Rep = findRep(ch1)
            ch2Rep = findRep(ch2)
            
            if size[ch1] <= size[ch2]:
                rep[ch1Rep] = ch2Rep
                size[ch2Rep] += size[ch1Rep]              
            else:
                rep[ch2Rep] = ch1Rep
                size[ch1Rep] += size[ch2Rep]     
                
        def connected(ch1, ch2):
            return findRep(ch1) == findRep(ch2)
        
        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3])
        
        for eq in equations:
            if eq[1] == "!":
                if connected(eq[0], eq[3]):
                    return False
        
        return True