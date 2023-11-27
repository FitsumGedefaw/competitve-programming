class Solution:
    def minTimeToType(self, word: str) -> int:
        minTime = 0
        ptrCh = "a"
        for ch in word:
            if ch == ptrCh:
                minTime += 1
            else:
                if ord(ptrCh) < ord(ch):
                    clockwise = ord(ch) - ord(ptrCh)
                    ctrClockwise = ord("z") - ord(ch) + ord(ptrCh) - ord("a") + 1
                else:
                    clockwise = ord(ptrCh) - ord(ch)
                    ctrClockwise = ord("z") - ord(ptrCh) + ord(ch) - ord("a") + 1
                minTime += min(clockwise, ctrClockwise) + 1
                ptrCh = ch

        return minTime
