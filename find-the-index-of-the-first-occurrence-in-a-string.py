class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        st = i = 0
        j = 0

        while st < len(haystack):
            j = st
            while i < len(needle) and j < len(haystack) and needle[i] == haystack[j]:
                i, j = i+1, j+1
            
            if i < len(needle):
                i = 0
                st += 1
            else:
                return st

        return -1