class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        @lru_cache(maxsize = None)

        def isSub(word):
            idx = -1
            for ch in word:
                idx = s.find(ch, idx+1)
                if idx == -1:
                    return False
            return True

        ans = 0
        for word in words:
            if isSub(word):
                ans += 1
        
        return ans