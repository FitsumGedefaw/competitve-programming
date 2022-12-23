class Solution:
    def longestPrefix(self, str1, str2):
        res = ""
        
        for i in range(len(min(str1, str2))):
            if str1[i] == str2[i]:
                res += str1[i]
            
            else: 
                break
                
        return res
                     
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        
        for i in range(1, len(strs)):
            ans = self.longestPrefix(ans, strs[i])
            
            if ans == "":
                return ""
        
        return ans
            
            
        