class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charsSet = set()
        maxLength = 0
        i = j = 0
        while j < len(s):
            if s[j] not in charsSet:
                charsSet.add(s[j])
                maxLength = max(maxLength, len(charsSet))
                j += 1
            else:
                charsSet.remove(s[i])
                i += 1
        return maxLength
            
