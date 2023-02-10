class Solution:
    def compress(self, chars: List[str]) -> int:
        insertIdx = 0
        i = 0
        
        while i < len(chars):
            chars[insertIdx] = chars[i]
            insertIdx += 1
            
            ct = 1
            while i < len(chars)-1 and chars[i] == chars[i+1]:
                ct += 1
                i += 1
                
            if ct > 1:
                for digit in str(ct):
                    chars[insertIdx] = digit
                    insertIdx += 1
                    
            i += 1
            
        return insertIdx
                    
                    
            
            