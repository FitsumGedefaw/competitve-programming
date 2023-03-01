class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        s = list(s)
        netShifts = [0] * len(s)
        
        for start, end, d in shifts:
            if d == 1:
                netShifts[start] += 1
                if end < len(netShifts)-1:
                    netShifts[end+1] -= 1
                    
            else:
                netShifts[start] -= 1
                if end < len(netShifts)-1:
                    netShifts[end+1] += 1
                    
        _sum = 0
        for i in range(len(netShifts)):
            _sum += netShifts[i]
            netShifts[i] = _sum
            
        print(netShifts)
            
        for i in range(len(s)):
            newPos = (alphabet.index(s[i]) + netShifts[i]) % 26
            s[i] = alphabet[newPos]
            
        return "".join(s)