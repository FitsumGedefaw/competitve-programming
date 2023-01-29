class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        
        merge = ""
        
        while i < len(word1) or j < len(word2):
            
            if i < len(word1) and j < len(word2):
                if word1[i] > word2[j]:
                    merge += word1[i]
                    i += 1
                    
                elif word1[i] < word2[j]:
                    merge += word2[j]
                    j += 1
                
                else:
                    if word1[i:] >= word2[j:]:
                        merge += word1[i]
                        i += 1
                    
                    else:
                        merge += word2[j]
                        j += 1

            elif i < len(word1):
                merge += word1[i]
                i += 1
                
            else: 
                merge += word2[j]
                j += 1
                
        return merge
                
                        
                        
                    
                    
                    